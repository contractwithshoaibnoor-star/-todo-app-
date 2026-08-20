# AI Chatbot Web App

A Flask web application that wraps an LLM API and gives the chatbot a custom personality via a system prompt. Project 7 of the Python Developer Roadmap.

## Features
- Chat UI with message history and copy buttons
- Server-side chat endpoint with conversation memory
- Custom system prompt configurable via environment variable
- Reset button to clear conversation
- Error handling for API failures and network issues
- Thinking indicator while waiting for responses

## Tech Stack
- Python 3, Flask, OpenAI Python SDK, HTML/CSS/JS, python-dotenv

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` (see below)
3. For Ollama: `ollama pull qwen2.5:0.5b`
4. Run: `python app.py`
5. Visit: `http://127.0.0.1:5000`

## Environment Configuration
```
API_PROVIDER=ollama
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL_NAME=qwen2.5:0.5b
SYSTEM_PROMPT=You are a friendly Python tutor for absolute beginners.
OPENAI_API_KEY=your-key-here
```

## Project Structure
- app.py - Flask application
- templates/index.html - Chat UI HTML + JavaScript
- static/style.css - Chat UI styling
- .env - Environment variables (not committed)

## Milestones Completed
- API hello-world
- Flask endpoint with /chat route
- Conversation history and memory
- Polish: loading indicator, reset button, error states

## Stretch Goals
- Streaming responses
- SQLite conversation history
- Multiple persona selection

## License
MIT
</parameter>
</invoke>
</dots_function_call>