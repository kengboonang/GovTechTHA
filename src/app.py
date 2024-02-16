# Description: Streamlit app for LLM-chat interface
import streamlit as st
from chatgpt import ChatGPT
import os

# create a ChatGPT instance
chat = ChatGPT()

# Setting page description
st.set_page_config(page_title="LLM Chatbot app", page_icon=":smiley:")
st.markdown("<h1 style='text-align: center; color: white;'>What would you like to talk about today?</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<h3 style='text-align: center; color: white;'>This Chatbot aims to help someone complete their take-home assignment because they have not enough frontend knowledge...</h3>", unsafe_allow_html=True)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Setting up the sidebar
st.sidebar.title("LLM Chatbot")
counter_placeholder = st.sidebar.empty()
with st.sidebar:
    st.markdown("<h3 style='text-align: center; color: white;'>This sidebar exists solely to house this button and hide it if the user doesn't wish to accidentally press the reset button.</h3>", unsafe_allow_html=True)
    clear_button = st.button("Clear history")

if clear_button:
    st.session_state.messages = []
    st.session_state.history = []
    counter_placeholder.empty()

# Main chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Query input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    
    with st.chat_message('assistant'):
        stream = chat.generate("assistant", prompt, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": stream})
        response = st.write(stream)

# print(st.session_state.messages)