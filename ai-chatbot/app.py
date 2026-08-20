import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Determine API provider from environment
API_PROVIDER = os.getenv("API_PROVIDER", "ollama")

if API_PROVIDER == "openai":
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = None
else:
    api_key = os.getenv("API_KEY", "ollama")
    base_url = os.getenv("BASE_URL", "http://localhost:11434/v1")

client_kwargs = {"api_key": api_key}
if base_url:
    client_kwargs["base_url"] = base_url

client = OpenAI(**client_kwargs)

MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:0.5b")

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are a friendly and helpful local AI assistant. "
    "Keep answers simple and helpful."
)

chat_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "error": "Message is empty"
        }), 400

    # Direct answer for identity questions
    identity_words = [
        "what is your name",
        "what's your name",
        "who are you",
        "your name",
        "what are you",
        "who r u"
    ]

    if any(word in user_message.lower() for word in identity_words):

        reply = "I am a local AI assistant running with Qwen through Ollama."

        chat_history.append({
            "role": "user",
            "content": user_message
        })

        chat_history.append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({
            "reply": reply
        })

    # Add user message
    chat_history.append({
        "role": "user",
        "content": user_message
    })

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=chat_history,
            temperature=0.2
        )

        reply = response.choices[0].message.content

        chat_history.append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        chat_history.pop()

        return jsonify({
            "error": "AI response failed",
            "details": str(e)
        }), 500


@app.route("/reset", methods=["POST"])
def reset():

    global chat_history

    chat_history = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    return jsonify({
        "message": "Chat reset successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)