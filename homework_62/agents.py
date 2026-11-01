import os
from pathlib import Path
from typing import TypedDict

from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph


MODEL = "gemini-2.5-flash"


class TravelState(TypedDict):
    user_request: str
    destination_info: str
    food_info: str
    budget_info: str
    final_plan: str


def load_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    for env_path in (
        Path(__file__).with_name(".env"),
        Path(__file__).parent.parent / "homework_60" / ".env",
        Path(__file__).parent.parent / "homework_54" / ".env",
    ):
        api_key = dotenv_values(env_path).get("GEMINI_API_KEY")
        if api_key:
            return api_key

    raise RuntimeError(
        "GEMINI_API_KEY is not set. Add it to homework_62/.env, "
        "homework_60/.env, or homework_54/.env."
    )


def create_model() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=load_api_key(),
        temperature=0,
    )


def destination_agent(user_request: str, model: ChatGoogleGenerativeAI) -> str:
    prompt = f"""
    You are the destination and activities specialist.
    Identify the destination and trip length from the user's request.
    Recommend relevant attractions and activities that match the
    user's interests. Focus on destinations and activities only;
    do not make food or budget recommendations and do not create the
    full itinerary. Do not claim live availability or invent facts.
    Reply in the same language as the user.

    User request:
    {user_request}
    """
    response = model.invoke(prompt)
    return str(response.text)


def food_agent(user_request: str, model: ChatGoogleGenerativeAI) -> str:
    prompt = f"""
    You are the local food specialist.
    Recommend local dishes and practical types of places to eat at
    the destination, taking the user's stated budget and preferences
    into account. Focus only on food; do not plan activities or the
    full trip. Do not invent specific restaurant details or claim
    current prices. Reply in the same language as the user.

    User request:
    {user_request}
    """
    response = model.invoke(prompt)
    return str(response.text)


def budget_agent(user_request: str, model: ChatGoogleGenerativeAI) -> str:
    prompt = f"""
    You are the travel budget specialist.
    Estimate the trip costs using the destination, trip length, and
    budget preference in the user's request. Separate the estimate
    into accommodation, food, local transport, and activities.
    State the currency and assumptions. Make clear that estimates
    are approximate and not live quotes. Do not recommend attractions
    or restaurants or write the full itinerary. Reply in the same
    language as the user.

    User request:
    {user_request}
    """
    response = model.invoke(prompt)
    return str(response.text)


def planner_agent(state: TravelState, model: ChatGoogleGenerativeAI) -> str:
    prompt = f"""
    You are the final travel planner. Combine the three specialist
    results below into one clear, practical travel plan. Include a
    short day-by-day outline suited to the requested trip length,
    food suggestions, and the budget breakdown. Use only information
    in the user request and specialist results; do not invent new
    attractions, restaurants, prices, or facts. Preserve caveats
    about estimates. Reply in the same language as the user.

    User request:
    {state["user_request"]}

    Destination specialist:
    {state["destination_info"]}

    Food specialist:
    {state["food_info"]}

    Budget specialist:
    {state["budget_info"]}
    """
    response = model.invoke(prompt)
    return str(response.text)


def build_graph(model: ChatGoogleGenerativeAI):
    def run_destination(state: TravelState) -> dict[str, str]:
        return {
            "destination_info": destination_agent(state["user_request"], model)
        }

    def run_food(state: TravelState) -> dict[str, str]:
        return {"food_info": food_agent(state["user_request"], model)}

    def run_budget(state: TravelState) -> dict[str, str]:
        return {"budget_info": budget_agent(state["user_request"], model)}

    def run_planner(state: TravelState) -> dict[str, str]:
        return {"final_plan": planner_agent(state, model)}

    builder = StateGraph(TravelState)
    builder.add_node("destination_agent", run_destination)
    builder.add_node("food_agent", run_food)
    builder.add_node("budget_agent", run_budget)
    builder.add_node("planner_agent", run_planner)

    builder.add_edge(START, "destination_agent")
    builder.add_edge(START, "food_agent")
    builder.add_edge(START, "budget_agent")
    builder.add_edge(
        ["destination_agent", "food_agent", "budget_agent"],
        "planner_agent",
    )
    builder.add_edge("planner_agent", END)
    return builder.compile()
