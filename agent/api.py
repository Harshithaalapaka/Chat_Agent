from fastapi import FastAPI
from pydantic import BaseModel
from llm import chat

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/ask")
def ask(data: ChatRequest):
    reply = chat(data.message)
    return {"response": reply}