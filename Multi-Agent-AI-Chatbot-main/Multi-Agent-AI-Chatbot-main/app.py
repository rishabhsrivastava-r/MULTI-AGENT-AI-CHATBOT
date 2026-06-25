import streamlit as st
from memory import add_memory
from coordinator import decide_agent

st.set_page_config(page_title="Multi-Agent AI Chatbot")

st.title("Multi-Agent AI Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask something")

if prompt:
    # Save user message
    add_memory(st.session_state["messages"], "user", prompt)

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    response = decide_agent(st.session_state["messages"], prompt)

    # Save assistant response
    add_memory(st.session_state["messages"], "assistant", response)

    with st.chat_message("assistant"):
        st.write(response)