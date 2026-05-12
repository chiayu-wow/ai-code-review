# AI Code Review Bot

An AI-powered code review tool built with FastAPI and Groq (LLaMA 3).

## Tech Stack
- Python + FastAPI
- Groq API (llama-3.1-8b-instant)
- Pydantic
- Docker (coming soon)
- React (coming soon)

## Project Structure

```
backend/
├── main.py
├── routers/
│   └── review.py
├── services/
│   └── Groq.py
└── models/
    └── review.py
```

## Getting Started

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn groq python-dotenv
```

Add your API key to `.env`:
```
GROQ_API_KEY=your_key_here
```

Run the server:
```bash
uvicorn main:app --reload
```

API docs: `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/review/ | Submit code for AI review |

## Request Example

```json
{
  "code": "your code here",
  "language": "python"
}
```

## Response Example

```json
{
  "language": "python",
  "review": "Overall review here",
  "suggestions": [
    "suggestion 1",
    "suggestion 2"
  ]
}
```