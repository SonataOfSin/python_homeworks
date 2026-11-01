from pydantic import BaseModel, Field, field_validator


class TravelRequest(BaseModel):
    request: str = Field(min_length=1, max_length=10_000)

    @field_validator("request")
    @classmethod
    def strip_request(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Request cannot be blank.")
        return value


class AgentResponse(BaseModel):
    agent: str
    result: str


class TravelPlanResponse(BaseModel):
    request: str
    destination_info: str
    food_info: str
    budget_info: str
    final_plan: str
