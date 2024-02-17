# Description: This file contains the FastAPI implementation.
from fastapi import FastAPI, Response, status
from pydantic import UUID4
from typing import Optional, List
import uuid
import uvicorn

from schemas.queries_schema import Prompt
from schemas.conversation_schema import Conversation, ConversationFull, ConversationPOST, ConversationPUT
from chatgpt import ChatGPT

app = FastAPI()

# Testing Code to check FastAPI implementation
@app.get("/")
def get_root():
    return {"message": "Hello World!"}

# Defining Backend APIs & Routes
@app.post("/conversations", status_code=status.HTTP_201_CREATED, tags=["Conversations"], response_model=ConversationPOST, summary="Create a new conversation", description="A Conversation describes a series of interactions with an LLM model. It also contains the properties that will be used to send individual queries to the LLM. Chat queries will be anonymised and logged for audit purposes.")
def create_conversation():
    # create a new conversation in the database
    # create a unique id for the conversation
    new_id = str(uuid.uuid4())
    # create model for the new conversation
    new_conversation = Conversation(id=new_id, name="New Conversation", params={}, tokens=0, messages=[])
    # add conversation to database
    # if successful, return the conversation
    # else, raise an error
    return {"id": new_id}

@app.get("/conversations", status_code=status.HTTP_200_OK, response_model=List[Conversation], tags=["Conversations"], summary="Retrieve a user's Conversation", description="Retrieves all the conversations that a user has created, the conversation history is not provided here.")
async def get_conversations():
    # search for all conversations in the database
    # if successful, return all conversations
    # else, raise an error
    return

@app.put("/conversations/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=ConversationPUT, tags=["Conversations"], summary="Updates the LLM properties of a Conversations", description="Allows the user to customise parameters and properties of a Conversation, thereby customising their experience.")
async def update_conversation(id: UUID4):
    # search to see if the conversation exists
    # if it does, update the conversation in the database
    # else, raise an error
    return

@app.get("/conversations/{id}", status_code=status.HTTP_200_OK, response_model=ConversationFull, tags=["Conversations"], summary="Retrieves the Conversation History", description="Retrieves the entire conversation history with the LLM.")
async def get_conversation(id: UUID4):
    # search to see if the user id exists
    # if it does, search for all conversations in the database
    # else, raise an error
    return

@app.delete("/conversations/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Conversations"], summary="Deletes the Conversation", description="Deletes the entire conversation history with the LLM Model")
async def delete_conversation(id: UUID4):
    # search to see if the conversation exists
    # if it does, delete the conversation in the database
    # else, raise an error
    return

@app.post("/queries/{id}", tags=["LLM Queries"], status_code=201, summary="Create a new Prompt query to the LLM.", description="This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised.")
def create_query(id: int, prompt: Optional[Prompt] = None):
    chat = ChatGPT()
    unique_id = uuid.uuid4()
    response = chat.generate(prompt.role, prompt.content)
    return {"id": unique_id}

# Define error handlers
@app.exception_handler(status.HTTP_400_BAD_REQUEST)
async def invalid_parameters_error_handler(request, exc):
    return Response(code=400, content="Invalid parameters", status_code=status.HTTP_400_BAD_REQUEST)

@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found_error_handler(request, exc):
    return Response(content="Resource not found", status_code=status.HTTP_404_NOT_FOUND)

@app.exception_handler(status.HTTP_422_UNPROCESSABLE_ENTITY)
async def invalid_creation_error_handler(request, exc):
    return Response(content="Invalid creation", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def internal_server_error_handler(request, exc):
    return Response(content="Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

if __name__ == "__main__":
    app_module = "main:app"
    uvicorn.run(app_module, host="0.0.0.0", port=8000, reload=True)