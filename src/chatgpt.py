# Description: This file contains the ChatGPT class which is used to interact with the OpenAI GPT-3.5 API.
import openai
import os
from dotenv import load_dotenv

load_dotenv()

def check_openai_api_key(api_key):
    openai.api_key = api_key
    try:
        openai.Model.list()
    except openai.error.AuthenticationError as e:
        return False
    else:
        return True

# class ChatGPT(object):
#     def __init__(self, api_key):
#         openai.api_key = api_key

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_KEY")
    is_valid = check_openai_api_key(api_key)

    if is_valid:
        print("Valid OpenAI API key.")
    else:
        print("Invalid OpenAI API key.")