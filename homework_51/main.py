import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


MENTOR_INSTRUCTIONS = (
    "You are an experienced senior software engineer and programming mentor. "
    "Explain technical concepts clearly, adapt your explanations to the user's "
    "level, and use practical examples when appropriate."
)
MODEL = "gemini-3.1-flash-lite"


def show_history(messages):
    if not messages:
        print("No conversation yet.")
        return

    for role, text in messages:
        print(f"{role}:\n{text}\n")


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to your environment or .env file."
        )

    client = genai.Client(api_key=api_key)
    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=MENTOR_INSTRUCTIONS,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            ),
        ),
    )
    messages = []

    while True:
        question = input("You: ").strip()

        if question.casefold() == "exit":
            print("\nGoodbye!")
            break

        if question.casefold() == "history":
            print()
            show_history(messages)
            continue

        if not question:
            continue

        response = chat.send_message(question)
        answer = response.text
        if answer is None:
            raise RuntimeError("The AI returned no text response.")

        messages.append(("USER", question))
        messages.append(("ASSISTANT", answer))
        print(f"\nAI: {answer}\n")


if __name__ == "__main__":
    main()
