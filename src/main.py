from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Union, List

app = FastAPI()

# Testing Code to check FastAPI implementation
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# APIs to implement for Take-home assignment
class Conversation(BaseModel):
    id: str
    history: List[str]

@app.post("/conversations", tags=["Conversations"], summary="Creates a new Conversation with an LLM model",
          description="A Conversation describes a series of interactions with an LLM model. It also contains the properties that will be used to send individual queries to the LLM. Chat queries will be anonymised and logged for audit purposes",
          response_model=Conversation, status_code=201)
def create_conversation(conversation: Conversation):
    return conversation
