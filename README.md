# 🤖 LLM Chat API with Groq

A containerized conversational AI API powered by Groq's ultra-fast LLM inference, built with FastAPI and deployed with Docker. Supports multi-turn conversations with full memory context.

---

## 🚀 What it does

Send messages to the API and get intelligent AI responses — it remembers the full conversation history just like ChatGPT!

```
You  → "My name is Abdul"
AI   → "Nice to meet you, Abdul!"
You  → "What is my name?"
AI   → "Your name is Abdul!"  ← remembers context!
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| 🐳 Docker | Containerization |
| ⚡ FastAPI | REST API framework |
| 🧠 Groq API | Ultra-fast LLM inference |
| 🦙 LLaMA 3.3 70B | Large language model |
| 🐍 Python 3.13 | Programming language |
| 🦄 Uvicorn | ASGI server |

---

## 📁 Project Structure

```
llm-chat-api-groq/
├── app.py              # FastAPI app with Groq LLM integration
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container recipe
├── .env                # API keys (not pushed to GitHub)
└── .gitignore          # Protects secret keys
```

---

## ⚙️ Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Groq API Key](https://console.groq.com/) — free to get!

---

## 🏃 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Abdul769469/llm-chat-api-groq.git
cd llm-chat-api-groq
```

### 2. Add your Groq API key
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Build the Docker image
```bash
docker build -t llm-chat-api .
```

### 4. Run the container
```bash
docker run -p 8000:8000 llm-chat-api
```

---

## 📡 API Endpoints

### `GET /`
Health check — confirms the server is running.

**Response:**
```json
{"status": "running"}
```

---

### `POST /chat`
Send a message and get an AI response with full conversation memory.

**Request body:**
```json
{
  "message": "What is Docker?"
}
```

**Response:**
```json
{
  "reply": "Docker is a platform that allows you to...",
  "total_messages": 2
}
```

---

### `GET /history`
Get the full conversation history.

**Response:**
```json
{
  "history": [
    {"role": "user", "content": "What is Docker?"},
    {"role": "assistant", "content": "Docker is a platform..."}
  ]
}
```

---

### `DELETE /reset`
Reset and clear the conversation history.

**Response:**
```json
{"status": "conversation reset"}
```

---

## 🖥️ Interactive API Docs

FastAPI automatically generates interactive documentation. Once the container is running, open your browser and go to:

```
http://localhost:8000/docs
```

---

## 💬 Example Conversation

```bash
# Start a conversation
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"My name is Abdul\"}"

# Test memory
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"What is my name?\"}"

# Check history
curl http://localhost:8000/history

# Reset conversation
curl -X DELETE http://localhost:8000/reset
```

---

## 🧠 How Conversation Memory Works

Every message is stored in a history list and sent to Groq with each request:

```
Request 1: [system] + [user: "My name is Abdul"]
Request 2: [system] + [user: "My name is Abdul"] + [assistant: "Nice to meet you!"] + [user: "What is my name?"]
```

This gives the model full context of the conversation!

---

## 🐳 Docker Commands Reference

| Command | Description |
|---|---|
| `docker build -t llm-chat-api .` | Build the image |
| `docker run -p 8000:8000 llm-chat-api` | Run the container |
| `docker ps` | List running containers |
| `docker stop <container_id>` | Stop a container |

---

## 👨‍💻 Author

**Abdul** — Built as part of an AI Engineer learning journey.

---

## 📄 License

MIT License