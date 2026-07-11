import streamlit as st
import google.generativeai as genai

st.title("📚 Study Buddy - DSA Tutor")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

system_prompt = """You are a friendly, patient tutor helping a 2nd year Computer Science student learn Data Structures and Algorithms.

Rules:
- Explain concepts clearly with simple examples
- If asked to solve a coding problem, give hints and guide their thinking — don't just hand over the full solution
- Keep answers concise and beginner-friendly
- Encourage the student when they get something right
"""

model = genai.GenerativeModel('gemini-flash-lite-latest', system_instruction=system_prompt)

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me anything about DSA...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = st.session_state.chat.send_message(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)
