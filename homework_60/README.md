# Homework 60: Multi-Agent Travel Planner

A LangGraph travel planner with three focused agents that analyze the
destination, local food, and estimated budget in parallel. A planner agent
combines their results into a single day-by-day trip plan.

## Setup

1. Install dependencies from the workspace root:

   ```bash
   python -m pip install -r homework_60/requirements.txt
   ```

2. Copy `homework_60/.env.example` to `homework_60/.env` and set
   `GEMINI_API_KEY` to your Google AI API key. Alternatively, the key can be
   read from `homework_54/.env`.

## Run

From the workspace root:

```bash
python homework_60/main.py
```

Enter a travel request when prompted, or press Enter to use the sample
four-day Paris request. The specialist results are joined before the planner
agent runs. Budget figures are approximate model-generated estimates, not
live prices.
