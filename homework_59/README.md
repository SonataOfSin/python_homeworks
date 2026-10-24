# Homework 59: LangGraph Recipe Generator

A LangGraph recipe generator that drafts a recipe from the provided
ingredients, checks it with an LLM, and improves it when the review does not
approve it. The graph stops when the recipe is approved or after three drafts.

## Setup

1. Install dependencies from the workspace root:

   ```bash
   python -m pip install -r homework_59/requirements.txt
   ```

2. Copy `homework_59/.env.example` to `homework_59/.env` and set
   `GEMINI_API_KEY` to your Google AI API key. Alternatively, the key can be
   read from `homework_54/.env`.

## Run

From the workspace root:

```bash
python homework_59/main.py
```

The program prints the final recipe and the latest review feedback.
