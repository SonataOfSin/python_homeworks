import os
from pathlib import Path
from typing import TypedDict

from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph


MODEL = "gemini-2.5-flash"


class State(TypedDict):
    product_text: str
    product_info: str
    marketing_text: str
    final_description: str


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
        "GEMINI_API_KEY is not set. Add it to homework_58/.env "
        "or homework_54/.env."
    )


def build_graph(model: ChatGoogleGenerativeAI):
    def extract(state: State) -> dict[str, str]:
        prompt = f"""
        Extract the product facts from this unorganized description.
        Return a concise, labeled list. Include only facts in the input;
        do not guess or add details.

        Product description:
        {state["product_text"]}
        """
        response = model.invoke(prompt)
        return {"product_info": response.text}

    def marketing(state: State) -> dict[str, str]:
        prompt = f"""
        Write polished, appealing online-store product copy using only
        the supplied product information. Do not invent features,
        specifications, or claims.

        Product information:
        {state["product_info"]}
        """
        response = model.invoke(prompt)
        return {"marketing_text": response.text}

    def format_description(state: State) -> dict[str, str]:
        return {
            "final_description": (
                "=== PRODUCT DESCRIPTION ===\n\n"
                f"{state['marketing_text']}\n\n"
                "=== END ==="
            )
        }

    graph = StateGraph(State)
    graph.add_node("extract", extract)
    graph.add_node("marketing", marketing)
    graph.add_node("format", format_description)
    graph.add_edge(START, "extract")
    graph.add_edge("extract", "marketing")
    graph.add_edge("marketing", "format")
    graph.add_edge("format", END)
    return graph.compile()


def main() -> None:
    model = ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=load_api_key(),
        temperature=0,
    )
    graph = build_graph(model)
    initial_state: State = {
        "product_text": (
            "iphone 15, 6.1 inch oled, 128gb, a16 bionic, 48mp camera, "
            "usb-c, battery good, available in black and blue"
        ),
        "product_info": "",
        "marketing_text": "",
        "final_description": "",
    }
    result = graph.invoke(initial_state)
    print(result["final_description"])


if __name__ == "__main__":
    main()
