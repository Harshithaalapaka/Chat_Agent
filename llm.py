
import os
from groq import Groq
from dotenv import load_dotenv
from storage import save_conversation, get_conversation_history

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(api_key=GROQ_API_KEY)

def chat_agent(user_input: str) -> str:
    
    save_conversation("user", user_input)

    
    history = get_conversation_history()

    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful,polite and professional customer support assistant. Be concise and answer in 1-3 sentences. Use previous conversation context when answering."
            },
            {
                "role": "user",
                "content": f"""
Conversation history:
{history}

User: {user_input}
"""
            }
        ],
        max_tokens=100,
        temperature=0.3
    )

    
    text = response.choices[0].message.content

    
    save_conversation("assistant", text)

    return text


chat = chat_agent
