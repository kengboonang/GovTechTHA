from pydantic import BaseModel, conint, constr, Field, ValidationError, UUID4
from typing import Dict, Optional, List
import uuid

from queries_schema import Prompt

class Params(BaseModel):
    """
    Parameter dictionary for overriding defaults prescribed by the AI Model
    """
    
class Conversation(BaseModel):
    """
    Representation of a series of interactions with a particular LLM
    """
    id: UUID4 = Field(..., description="ID of the conversation", readOnly=True)
    name: constr(max_length=200) = Field(..., description="Title of the conversation")
    params: Params
    tokens: conint(ge=0) = Field(..., description="Total number of tokens consumed in this entire Chat", readOnly=True)

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

if __name__ == "__main__":
    # test APIError class
    test_uuid = uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6")
    test_conversation = Conversation(
        id=test_uuid,
        name="Test Conversation",
        params=Params(),
        tokens=100
    )
    print(repr(test_conversation))