from fastapi import APIRouter, HTTPException , Response, status
from pydantic import BaseModel, validator
from typing import Optional
import uuid

from schemas.conversation_schema import Conversation, ConversationFull, ConversationPOST, ConversationPUT

router = APIRouter()

@router.post("/conversations", status_code=status.HTTP_201_CREATED, response_model=ConversationFull, summary="Create a new conversation", description="A Conversation describes a series of interactions with an LLM model. It also contains the properties that will be used to send individual queries to the LLM. Chat queries will be anonymised and logged for audit purposes.")
def create_conversation():
    new_id = str(uuid.uuid4())
    new_conversation = Conversation(id=new_id, name="New Conversation", params={}, tokens=0, messages=[])
    return {"id": new_id}