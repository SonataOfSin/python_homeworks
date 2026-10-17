import argparse
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


MODEL = "gemini-3.8-flash"
EXAMPLE_REVIEWS = [
    (
        "Test 1",
        "This laptop is fast, lightweight, and has an excellent display. "
        "However, its battery life could be better.",
    ),
    (
        "Test 2",
        "The phone is slow, overheats frequently, and the camera quality "
        "is disappointing.",
    ),
    (
        "Test 3",
        "The headphones have average sound quality. They are comfortable, "
        "but the price is relatively high.",
    ),
]


class ProductReviewAnalysis(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Overall review sentiment."
    )
    pros: list[str] = Field(description="Positive aspects mentioned in the review.")
    cons: list[str] = Field(description="Negative aspects mentioned in the review.")
    summary: str = Field(description="A short summary of the review.")
    recommend: bool = Field(
        description="Whether the reviewer recommends buying this product."
    )


output_parser = PydanticOutputParser(pydantic_object=ProductReviewAnalysis)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Analyze the user's product review and return an accurate structured "
            "assessment. Do not invent details that are not in the review. "
            "Choose positive, negative, or neutral for sentiment. Set recommend "
            "to true only when the review overall recommends buying the product. "
            "Follow these formatting instructions exactly:\n{format_instructions}",
        ),
        ("human", "{review}"),
    ]
).partial(format_instructions=output_parser.get_format_instructions())


def build_chain(api_key: str):
    model = ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=api_key,
        temperature=0,
    )
    return prompt | model | output_parser


def get_reviews(run_examples: bool) -> list[tuple[str, str]]:
    if run_examples:
        return EXAMPLE_REVIEWS

    review = input("Enter a product review: ").strip()
    if not review:
        raise ValueError("The product review cannot be empty.")
    return [("Product review", review)]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze product reviews with LangChain and Gemini."
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Analyze the three sample product reviews.",
    )
    args = parser.parse_args()

    load_dotenv(Path(__file__).with_name(".env"))
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to homework_54/.env.")

    chain = build_chain(api_key)
    for label, review in get_reviews(args.examples):
        result = chain.invoke({"review": review})
        print(f"\n=== {label} ===")
        print(result)
        print(f"Data type: {type(result).__name__}")


if __name__ == "__main__":
    main()
