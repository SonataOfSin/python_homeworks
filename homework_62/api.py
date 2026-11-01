from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from langchain_google_genai import ChatGoogleGenerativeAI

from .agents import (
    build_graph,
    budget_agent,
    create_model,
    destination_agent,
    food_agent,
)
from .schemas import AgentResponse, TravelPlanResponse, TravelRequest


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = create_model()
    app.state.model = model
    app.state.graph = build_graph(model)
    yield


app = FastAPI(
    title="Multi-Agent Travel Planner",
    description=(
        "Plan a trip with destination, food, and budget specialists "
        "working together."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


def get_model(request: Request) -> ChatGoogleGenerativeAI:
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="The travel planner service is not initialized.",
        )
    return model


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "service": "Multi-Agent Travel Planner",
        "status": "running",
        "docs": "/docs",
    }


@app.post("/api/agents/destination", response_model=AgentResponse)
def run_destination(
    travel_request: TravelRequest,
    request: Request,
) -> AgentResponse:
    result = destination_agent(travel_request.request.strip(), get_model(request))
    return AgentResponse(agent="destination", result=result)


@app.post("/api/agents/food", response_model=AgentResponse)
def run_food(travel_request: TravelRequest, request: Request) -> AgentResponse:
    result = food_agent(travel_request.request.strip(), get_model(request))
    return AgentResponse(agent="food", result=result)


@app.post("/api/agents/budget", response_model=AgentResponse)
def run_budget(travel_request: TravelRequest, request: Request) -> AgentResponse:
    result = budget_agent(travel_request.request.strip(), get_model(request))
    return AgentResponse(agent="budget", result=result)


@app.post("/api/travel-plan", response_model=TravelPlanResponse)
def create_travel_plan(
    travel_request: TravelRequest,
    request: Request,
) -> TravelPlanResponse:
    user_request = travel_request.request.strip()
    if not user_request:
        raise HTTPException(status_code=422, detail="Request cannot be blank.")

    graph = getattr(request.app.state, "graph", None)
    if graph is None:
        raise HTTPException(
            status_code=503,
            detail="The travel planner service is not initialized.",
        )

    initial_state = {
        "user_request": user_request,
        "destination_info": "",
        "food_info": "",
        "budget_info": "",
        "final_plan": "",
    }
    result = graph.invoke(initial_state)
    return TravelPlanResponse(
        request=user_request,
        destination_info=result["destination_info"],
        food_info=result["food_info"],
        budget_info=result["budget_info"],
        final_plan=result["final_plan"],
    )
