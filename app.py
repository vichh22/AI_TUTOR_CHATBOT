
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from groq import Groq
import os
import json

# --------------------------------------------------
# Initialize Flask
# --------------------------------------------------

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "chat_history.json")

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv(os.path.join(BASE_DIR, ".env"))

api_key = os.getenv("Groq_api_key")

if not api_key:
    raise ValueError(
        "Groq API key not found. Check your .env file."
    )

client = Groq(api_key=api_key)

# --------------------------------------------------
# System instruction
# --------------------------------------------------

system_message = {
    "role": "system",
    "content": """
You are a friendly AI teacher.

Rules:
- Explain concepts in simple English.
- Give simple examples.
- Keep answers clear and beginner-friendly.
- Use previous conversation context when relevant.
"""
}


# --------------------------------------------------
# Load conversation history
# --------------------------------------------------

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        # Keep only valid user and assistant messages.
        return [
            message for message in data
            if isinstance(message, dict)
            and message.get("role") in ("user", "assistant")
            and isinstance(message.get("content"), str)
        ]

    except (json.JSONDecodeError, OSError):
        return []


def save_history(messages):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)


# --------------------------------------------------
# Serve the HTML UI
# --------------------------------------------------

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


# --------------------------------------------------
# Chat API
# --------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    prompt = data.get("message", "")

    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({"reply": "Please enter a message."}), 400

    prompt = prompt.strip()

    try:
        # Load previous conversation
        messages = load_history()

        # Add the current user message
        messages.append({
            "role": "user",
            "content": prompt
        })

        # Keep recent conversation context
        recent_messages = [
            system_message
        ] + messages[-10:]

        # Send request to Groq
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=recent_messages,
            stream=True,
            include_reasoning=False
        )

        # Collect the streamed response
        answer = ""

        for chunk in response:
            content = chunk.choices[0].delta.content

            if content:
                answer += content

        # Save the AI response
        messages.append({
            "role": "assistant",
            "content": answer
        })

        save_history(messages)

        return jsonify({"reply": answer})

    except Exception as error:
        app.logger.exception("Groq chat request failed")

        return jsonify({
            "reply": "Sorry, something went wrong while generating your answer. Please try again."
        }), 500


# --------------------------------------------------
# Run Flask
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

