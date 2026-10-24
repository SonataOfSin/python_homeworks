# Homework 58: AI Product Description Pipeline

A linear LangGraph pipeline that extracts product facts from an unorganized
description, writes marketing copy, and formats the final online-store
description.

## Setup

1. Install dependencies from the workspace root:

   ```bash
   python -m pip install -r homework_58/requirements.txt
   ```

2. Copy `homework_58/.env.example` to `homework_58/.env` and set
   `GEMINI_API_KEY` to your Google AI API key. Alternatively, the key can be
   read from `homework_54/.env`.

## Run

From the workspace root:

```bash
python homework_58/main.py
```

The program runs the product text through `extract`, `marketing`, and `format`
nodes in order, then prints the final description.
