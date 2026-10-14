# AI Teacher Chatbot

An AI-powered educational chatbot that helps users learn technical and general concepts through simple explanations and practical examples. The chatbot uses the Groq API to generate responses and provides a web-based interface built with HTML, CSS, JavaScript, and Flask.

## Features

- **AI-powered learning:** Get answers to questions using a Groq-hosted language model.
- **Beginner-friendly explanations:** Understand concepts through simple English and examples.
- **Interactive web interface:** Chat through a clean, responsive user interface.
- **Conversation context:** Use recent messages to maintain conversational context.
- **Chat history:** Save conversations locally in a JSON file.
- **Secure API configuration:** Store API credentials in environment variables.
- **Python backend:** Handle chat requests and AI responses using Flask.

## Technologies Used

- **Python** — Backend programming
- **Flask** — Web application framework
- **Groq API** — AI response generation
- **HTML5** — Web page structure
- **CSS3** — Styling and responsive design
- **JavaScript** — Chat interactions and API requests
- **JSON** — Conversation history storage
- **python-dotenv** — Environment variable management

## Project Structure

```text
Chat_bot_demo/
│
├── .venv/                  # Python virtual environment
├── .vscode/                # VS Code settings (optional)
├── Data/                   # Project data, if required
├── .env                    # API key configuration (not committed)
├── .gitignore              # Git exclusion rules
├── app.py                  # Flask backend and chat API
├── main.py                 # Python chatbot script
├── index.html              # Chatbot frontend
├── chat_history.json       # Saved conversations (not committed)
├── file_handling_demo.py   # File handling demonstration
└── README.md               # Project documentation
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or a compatible version
- Git (optional, for version control)
- A Groq API key
- An internet connection to access the Groq API

## Installation and Setup

### 1. Clone the repository

If the project is hosted on GitHub, run:

```bash
git clone <your-repository-url>
cd Chat_bot_demo
```

Alternatively, open your existing project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask groq python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root directory and add your Groq API key:

```dotenv
Groq_api_key=your_groq_api_key_here
```

Replace the placeholder with your actual API key.

**Security:** Never upload your `.env` file or expose your API key in frontend JavaScript or public repositories.

### 5. Run the application

Start the Flask backend:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You can now interact with the AI Teacher through the web interface.

## How It Works

1. The user enters a question in the chatbot interface.
2. JavaScript sends the message to the Flask `/chat` endpoint.
3. Flask sends the message and recent conversation context to the Groq API.
4. The AI model generates a response.
5. Flask returns the response to the frontend.
6. The conversation is saved in `chat_history.json`.

## API Endpoint

### Chat

**Endpoint:** `/chat`

**Method:** `POST`

**Request body:**

```json
{
  "message": "Explain artificial intelligence in simple English."
}
```

**Example response:**

```json
{
  "reply": "Artificial intelligence is a technology that enables computers to perform tasks that usually require human intelligence."
}
```

## Conversation History

The application stores conversations in `chat_history.json` so previous messages can be reused as context.

This file is generated or updated when conversations are saved. It may contain private information, so it should not be committed to a public repository.

## Git and Security

The `.gitignore` file should exclude files such as:

```gitignore
.env
.env.*
!.env.example
.venv/
venv/
__pycache__/
*.py[cod]
chat_history.json
.vscode/
```

Keep source files such as `app.py`, `main.py`, and `index.html` under version control.

## Troubleshooting

**API key not found**
- Verify that `.env` exists in the project root.
- Check that the variable name is `Groq_api_key`.
- Restart the application after changing environment variables.

**Module not found**
- Activate the virtual environment.
- Install dependencies using `pip install flask groq python-dotenv`.

**Unable to connect to the chatbot**
- Confirm that Flask is running.
- Open the application through `http://127.0.0.1:5000` rather than opening `index.html` directly.
- Check the Flask terminal for API errors.

**Model or API error**
- Verify that your Groq API key is valid.
- Check your model access, API limits, and network connection.

## Future Improvements

- Stream AI responses directly into the chat interface.
- Add user authentication and individual conversation histories.
- Support Markdown formatting and code highlighting.
- Add conversation deletion and export options.
- Improve error handling and loading indicators.
- Deploy the application to a suitable hosting platform.

## Author

**Project:** AI Teacher Chatbot

**Purpose:** To make learning easier through interactive, AI-powered explanations.

## License

This project is available for educational and personal learning purposes. Add a suitable open-source license, such as the MIT License, if you intend to distribute it under those terms.
