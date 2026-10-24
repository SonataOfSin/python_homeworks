import json
import os
from pathlib import Path
from typing import TypedDict

from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph


MODEL = "gemini-2.5-flash"
MAX_ATTEMPTS = 3


class State(TypedDict):
    ingredients: str
    recipe: str
    feedback: str
    approved: bool
    attempts: int


def load_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    api_key = dotenv_values(Path(__file__).with_name(".env")).get("GEMINI_API_KEY")
    if api_key:
        return api_key

    api_key = dotenv_values(
        Path(__file__).parent.parent / "homework_54" / ".env"
    ).get("GEMINI_API_KEY")
    if api_key:
        return api_key

    raise RuntimeError(
        "GEMINI_API_KEY is not set. Add it to homework_59/.env "
        "or homework_54/.env."
    )


def build_graph(model: ChatGoogleGenerativeAI):
    def generate_recipe(state: State) -> dict[str, str | int]:
        prompt = f"""
        Create a clear, practical recipe using the ingredients below.
        Include ingredient quantities, cooking time, and numbered
        preparation steps. Do not add main ingredients that were not listed.

        Ingredients:
        {state["ingredients"]}
        """
        response = model.invoke(prompt)
        return {"recipe": response.text, "attempts": 1}

    def check_recipe(state: State) -> dict[str, str | bool]:
        prompt = f"""
        Check this recipe for quality. Verify that it uses the listed
        ingredients, is clear, includes preparation steps and cooking time,
        and has sensible ingredient quantities.

        Ingredients:
        {state["ingredients"]}

        Recipe:
        {state["recipe"]}

        Return only a valid JSON object with exactly these fields:
        {{"approved": true or false, "feedback": "brief explanation"}}
        Set approved to true only if the recipe satisfies the checks.
        """
        response = model.invoke(prompt)
        try:
            review = json.loads(response.text)
        except json.JSONDecodeError as error:
            raise ValueError("The recipe review was not valid JSON.") from error

        if (
            not isinstance(review, dict)
            or not isinstance(review.get("approved"), bool)
            or not isinstance(review.get("feedback"), str)
        ):
            raise ValueError(
                "The recipe review must contain a boolean 'approved' "
                "and a string 'feedback'."
            )

        return {
            "feedback": review["feedback"],
            "approved": review["approved"],
        }

    def improve(state: State) -> dict[str, str | int]:
        prompt = f"""
        Improve the recipe by addressing the review feedback. Use the
        listed ingredients, include sensible quantities, cooking time,
        and clear preparation steps. Do not add unlisted main ingredients.

        Ingredients:
        {state["ingredients"]}

        Current recipe:
        {state["recipe"]}

        Feedback:
        {state["feedback"]}
        """
        response = model.invoke(prompt)
        return {
            "recipe": response.text,
            "attempts": state["attempts"] + 1,
        }

    def route_after_check(state: State) -> str:
        if state["approved"] or state["attempts"] >= MAX_ATTEMPTS:
            return END
        return "improve"

    builder = StateGraph(State)
    builder.add_node("generate_recipe", generate_recipe)
    builder.add_node("check_recipe", check_recipe)
    builder.add_node("improve", improve)
    builder.add_edge(START, "generate_recipe")
    builder.add_edge("generate_recipe", "check_recipe")
    builder.add_conditional_edges("check_recipe", route_after_check)
    builder.add_edge("improve", "check_recipe")
    return builder.compile()


def main() -> None:
    llm = ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=load_api_key(),
        temperature=0,
    )
    graph = build_graph(llm)
    result = graph.invoke(
        {
            "ingredients": "chicken, rice, onion, tomato",
            "recipe": "",
            "feedback": "",
            "approved": False,
            "attempts": 0,
        }
    )
    print("Recipe:")
    print(result["recipe"])
    print("\nFeedback:")
    print(result["feedback"])


if __name__ == "__main__":
    main()
