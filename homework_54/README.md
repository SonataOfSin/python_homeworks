# Homework 54: Product Review AI Assistant

Analyzes product reviews with LangChain, `ChatPromptTemplate`,
`PydanticOutputParser`, and Gemini. The structured result includes sentiment,
pros, cons, a short summary, and a recommendation.

## Setup

From this folder, install dependencies and copy the environment template:

```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
```

Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Run

Analyze one review:

```powershell
python main.py
```

Run the three assignment examples:

```powershell
python main.py --examples
```

The program prints the parsed Pydantic object and its Python data type.
