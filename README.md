# Market Trade Opportunity Analyzer

## Overview
This project is a FastAPI-based service that analyzes current market data and
provides AI-generated trade opportunity insights for specific sectors in India.
The service fetches recent market information from the web, analyzes it using
an LLM (Openai API), and returns a structured markdown report.

⚠️ This project provides analytical insights only and does not perform real
trading or financial advice.

---

## Tech Stack
- FastAPI
- Python 3.10+
- Openai API
- Web Search API (OpenAI internal tool)
- In-memory storage (no database)

---

## Features
- Single API endpoint for sector-based analysis
- Structured markdown market reports
- Guest authentication with session management
- Rate limiting per session
- Input validation using Enum
- Automatic API documentation via Swagger

---

## API Endpoint
GET `/trade/analyze/{sector}`

**Allowed sectors:**
- pharmaceuticals
- technology
- agriculture
- finance
- energy
- infrastructure

**Response:**
- Structured markdown report

## HOW To USE

```bash
# Clone the repository
with HTTPS:
git clone https://github.com/rajnagani31/Trade-Opportunity.git

with SSH:
git clone git@github.com:rajnagani31/Trade-Opportunity.git

git checkout master


```bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

# API Documentation

```bash
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc
```
### Analyze Sector
