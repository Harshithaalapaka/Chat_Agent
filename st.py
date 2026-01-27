# st_app.py
import streamlit as st
from llm import chat  # your chat function

st.set_page_config(page_title="Chat Agent", page_icon="🤖")

st.title("Chat Agent")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Function to send message
def send_message():
    user_msg = st.session_state.user_input.strip()
    if user_msg:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_msg})

        # Get bot reply
        bot_msg = chat(user_msg)  # Ensure your LLM prompt says "Be concise"
        st.session_state.messages.append({"role": "assistant", "content": bot_msg})

        # Clear input
        st.session_state.user_input = ""

# Function to exit chat
def exit_chat():
    st.session_state.messages = []
    st.session_state.user_input = ""
    st.success("Chat cleared. Session ended.")

# Display chat messages
for m in st.session_state.messages:
    if m["role"] == "user":
        st.markdown(
            f"<div style='background-color:#DCF8C6; padding:8px; border-radius:5px; margin:5px 0;'>"
            f"<b>You:</b> {m['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#F1F0F0; padding:8px; border-radius:5px; margin:5px 0;'>"
            f"<b>Bot:</b> {m['content']}</div>",
            unsafe_allow_html=True
        )

# Input box and buttons
st.text_input("Type your message:", key="user_input", on_change=send_message)
st.button("Exit", on_click=exit_chat)
