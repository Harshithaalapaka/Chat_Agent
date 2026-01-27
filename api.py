
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llm import chat 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Chat Agent API is running. Use POST /ask to chat."}


class ChatRequest(BaseModel):
    message: str


@app.post("/ask")
def ask(data: ChatRequest):
    reply = chat(data.message)
    return {"response": reply}
