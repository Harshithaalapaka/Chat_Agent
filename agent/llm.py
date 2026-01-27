# llm.py
from groq import GroqLLM
from dotenv import load_dotenv  
from db import save_conversation, get_conversation_history  
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = GroqLLM(
    api_key=GROQ_API_KEY,
    model="groq-llm",         
    temperature=0.3,
    max_tokens=1024
)

# Make chat_agent function same as before
def chat_agent(user_input: str) -> str:
    # Save user message
    save_conversation("user", user_input)

    # Get conversation history
    history = get_conversation_history()
    user_lower = user_input.lower()

    # Agent decision-making
    if user_lower in ["clear", "reset", "start over"]:
        # Optional: actually clear memory
        save_conversation("system", "Conversation cleared")
        response = "Conversation cleared. How can I help you now?"
    elif "remember" in user_lower:
        response = "Yes, I remember our previous conversation."
    elif len(user_input.split()) < 2:
        response = "Can you please give a little more detail?"
    else:
        prompt = f"""
You are an intelligent chat agent.
Use previous conversation to respond correctly.

Conversation history:
{history}

User: {user_input}
Assistant:
"""
        # 4️⃣ Get LLM response
        response = llm.complete(prompt)  
        response = response.text        

    # Save assistant reply
    save_conversation("assistant", response)

    return response


