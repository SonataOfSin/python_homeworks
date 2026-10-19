# Homework 56

This script reads the hotel information from `homework_55/hotel_info.md`, splits
it into chunks, embeds the chunks with Gemini, and stores them in PostgreSQL
using the `pgvector` extension. It retrieves the three nearest chunks by cosine
distance and passes them to Gemini to answer a question in the same language.

## Setup

1. Create a PostgreSQL database named `homework_56`.
2. Install PostgreSQL's `pgvector` extension for your PostgreSQL server. The
   database user must be allowed to run `CREATE EXTENSION`.
3. From the workspace root, install dependencies:

   ```powershell
   python -m pip install -r homework_56\requirements.txt
   ```

4. Copy `.env.example` to `.env` in this folder and set `GEMINI_API_KEY` and
   `DATABASE_URL` to your own values. The Gemini key can instead be read from
   `homework_54/.env`; the PostgreSQL URL must be set in the environment or
   `homework_56/.env`. Never commit `.env`.

## Run

From the workspace root:

```powershell
python homework_56\main.py
```

On the first run, the script embeds and saves the hotel chunks. Later runs reuse
the saved vectors. To rebuild the stored chunks after changing the source file:

```powershell
python homework_56\main.py --reindex
```
