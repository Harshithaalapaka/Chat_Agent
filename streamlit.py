import streamlit as st
from llm import chat 
st.set_page_config(page_title="Chat Agent")
st.title("Chat Agent")
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": chat()
    })

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def send_message():
    user_msg = st.session_state.user_input.strip()
    if user_msg:
        st.session_state.messages.append({"role": "user", "content": user_msg})
        bot_msg = chat(user_msg) 
        st.session_state.messages.append({"role": "assistant", "content": bot_msg})
        st.session_state.user_input = ""

def exit_chat():
    st.session_state.messages = []
    st.session_state.user_input = ""
    st.success("Chat cleared. Session ended.")

for m in st.session_state.messages:
    if m["role"] == "user":
        st.markdown(
            f"<div style='padding:8px; border-radius:5px; margin:5px 0;'>"
            f"<b>You:</b> {m['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='padding:8px; border-radius:5px; margin:5px 0;'>"
            f"<b>Bot:</b> {m['content']}</div>",
            unsafe_allow_html=True
        )

st.text_input("Type your message:", key="user_input", on_change=send_message)
st.button("Exit", on_click=exit_chat)
