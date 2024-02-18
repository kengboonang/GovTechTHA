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

# creating session states to store the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# if "api_key" not in st.session_state:
#     st.session_state.api_key = ""

# Setting up the sidebar
st.sidebar.title("LLM Chatbot")
counter_placeholder = st.sidebar.empty()
with st.sidebar:
    # st.markdown("<h3 style='text-align: center; color: white;'>Enter your api-key here if you are not using an environment variable to run the app.</h3>", unsafe_allow_html=True)
    # user_api_key = st.text_input("API Key", value=st.session_state.api_key)
    # use_key = st.button("Load API Key")
    # clear_key = st.button("Clear API Key")
    st.markdown("<h3 style='text-align: center; color: white;'>Clear chat history here</h3>", unsafe_allow_html=True)
    clear_button = st.button("Clear history")

# Managing user's api key
# if use_key:
#     st.session_state.api_key = user_api_key
#     chat.change_keys(api_key=st.session_state.api_key)
# if clear_key:
#     st.session_state.api_key = ""
#     chat = ChatGPT()

# Clearing history
if clear_button:
    st.session_state.messages = []
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