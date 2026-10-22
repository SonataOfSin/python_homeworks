# Homework 57: AI Travel Assistant

An interactive travel assistant built with LangChain and Gemini. The model
chooses whether to search sample hotels, look up a currency exchange rate, or
list attractions based on the user's question. Tool results are sent back to
the model before it produces its final answer.

## Setup

1. Install dependencies from the workspace root:

   ```powershell
   python -m pip install -r homework_57\requirements.txt
   ```

2. Copy `homework_57\.env.example` to `homework_57\.env` and set
   `GEMINI_API_KEY` to your Google AI API key. Alternatively, the key can be
   read from `homework_54\.env`.

## Run

From the workspace root:

```powershell
python homework_57\main.py
```

Enter a travel question when prompted. The sample hotel and attraction data is
for Tbilisi, Batumi, and Kutaisi. Exchange rates are example values, not live
financial data.
