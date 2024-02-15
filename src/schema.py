from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError, UUID4
from typing import Dict, Optional, Union, List

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

@app.get("/chat")
def read_chat(messages: List[Prompt]):
    return messages

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