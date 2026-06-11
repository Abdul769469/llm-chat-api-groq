from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

app = FastAPI()

# Connect to Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Store conversation history
conversation_history = []

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/chat")
def chat(request: ChatRequest):
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": request.message
    })
    
    # Send to Groq with full history
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."}
        ] + conversation_history
    )
    
    # Get reply
    reply = response.choices[0].message.content
    
    # Add AI reply to history
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    return {
        "reply": reply,
        "total_messages": len(conversation_history)
    }

@app.get("/history")
def get_history():
    return {"history": conversation_history}

@app.delete("/reset")
def reset():
    conversation_history.clear()
    return {"status": "conversation reset"}