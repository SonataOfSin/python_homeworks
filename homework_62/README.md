# Homework 62: FastAPI and Streamlit Travel Planner

This homework continues the Multi-Agent Travel Planner from
[homework 60](../homework_60/README.md). It preserves the parallel destination,
food, and budget specialists and the final planner, exposes them through
FastAPI, and provides a Streamlit interface.

## Setup

From the `python_homeworks-main` directory, install dependencies:

```bash
python -m pip install -r homework_62/requirements.txt
```

Set `GEMINI_API_KEY` in the environment or copy `.env.example` to `.env` inside
`homework_62` and add your key. For compatibility with the earlier homework,
the key is also read from `homework_60/.env` or `homework_54/.env`.

## Run

From the `python_homeworks-main` directory, start the API:

```bash
uvicorn homework_62.api:app --reload
```

In another terminal, launch the GUI:

```bash
streamlit run homework_62/streamlit_app.py
```

The API is available at `http://localhost:8000`; interactive API documentation
is at `http://localhost:8000/docs`. Set `API_BASE_URL` before starting
Streamlit if the API runs at a different address.

## Endpoints

- `GET /` — service status
- `POST /api/agents/destination` — destination and activity recommendations
- `POST /api/agents/food` — local food recommendations
- `POST /api/agents/budget` — approximate budget breakdown
- `POST /api/travel-plan` — full plan combining all specialists

POST requests accept JSON such as:

```json
{
  "request": "I want to spend four days in Paris, visit museums, and eat local food on a moderate budget."
}
```

The model's budget output is an estimate, not a live quote.
