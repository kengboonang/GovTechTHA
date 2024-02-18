from chatgpt import ChatGPT
from enum import Enum
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field, ValidationError, UUID4
from typing import Dict, Optional, Union, List

import uuid

app = FastAPI()
# Schemas
class request(BaseModel):
    """
    Request details associated with the error
    """
class details(BaseModel):
    """
    Other details associated with the error
    """

class APIError(BaseModel):
    """
    Generic schema for expressing API errors
    """
    code: int = Field(..., description="API Error code associated with the error")
    message: str = Field(..., description="API Error code associated with the error")
    request: Optional[request]
    details: Optional[details]


class QueryRoleType(str, Enum):
    """
    Chat roles for each individual message
    \nsystem = Message is a system message 
    \nuser = Message is a prompt from the user 
    \nassistant = Message is a reply from the LLM model 
    \nfunction = Message is a function call message
    """
    system = "system"
    user = "user"
    assistant = "assistant"
    function = "function"

class Prompt(BaseModel):
    """
    Prompt interaction structure
    """
    role: QueryRoleType
    content: str = Field(..., description="This is the prompt content of the message")

class Conversation(BaseModel):
    """
    Representation of a series of interactions with a particular LLM
    """
    id: UUID4 = Field(..., description="ID of the conversation", readOnly=True)
    name: str = Field(..., description="Title of the conversation", max_length=200)
    params: Dict[str, str] = Field(..., description="Parameter dictionary for overriding defaults prescribed by the AI Model")
    tokens: int = Field(..., description="Total number of tokens consumed in this entire Chat", ge=0, readOnly=True)

class ConversationFull(Conversation):
    """
    Complete Chat schema with messages
    """
    messages: List[Prompt] = Field(..., description="Chat messages to be included")

class ConversationPOST(BaseModel):
    """
    POST request for creating a new Chat
    """
    name: str = Field(..., description="Title of the conversation", max_length=200)
    params: Optional[Dict[str, str]] = Field(..., description="Parameter dictionary for overriding defaults prescribed by the AI Model")

class ConversationPUT(BaseModel):
    """
    PUT request for modifying a Chat
    """
    name: Optional[str] = Field(..., description="Title of the conversation", max_length=200)
    params: Optional[Dict[str, str]] = Field(..., description="Parameter dictionary for overriding defaults prescribed by the AI Model")

@app.get("/errors")
def read_error(APIError: APIError):
    return APIError

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

@app.post("/conversation")
def create_conversation(conversation: Conversation):
    return conversation

@app.post("/conversation/full")
def create_conversation_full(conversation: ConversationFull):
    return conversation

@app.post("/conversation/post")
def create_conversation_post(conversation: ConversationPOST):
    return conversation

@app.put("/conversation/put")
def modify_conversation(conversation: ConversationPUT):
    return conversation

if __name__ == "__main__":
    pass