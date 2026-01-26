from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from db import save_conversation, get_conversation_history  
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3,
    max_op_tokens=1024
)

def chat(user_input: str) -> str:
    save_conversation("user", user_input)
    conversation_history = get_conversation_history()
    prompt = f"""
      You are a polite and professional customer support assistant.
      Be clear, concise, and helpful.

      User: {user_input}
      Assistant:
"""
    response=llm.invoke(prompt)
    rply=response.content
    save_conversation("assistant", rply)
    return rply
