from enum import Enum
from fastapi import FastAPI, HTTPException , Response, status
from pydantic import BaseModel, validator
from typing import Optional

from chatgpt import ChatGPT

class Role(Enum):
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
    role: Role
    content: str

    @validator('role')
    def validate_role(cls, role):
        if role not in Role.__members__.values():
            raise ValueError('The role is not part of the Role Enum. Please use one of the following: system, user, assistant, function.')
        return role

app = FastAPI()

@app.post("/queries/{id}", status_code=status.HTTP_201_CREATED, response_model=Prompt, summary="Create a new query", description="This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised.")
def create_query(id: int, prompt: Optional[Prompt] = None):
    chat = ChatGPT()
    response = chat.generate(prompt.role, prompt.content) if prompt else None
    return {"id": id, "response": response}

if __name__ == "__main__":
    # test Prompt class
    test_prompt = Prompt(
        role=Role.system, 
        content="Hello, World!"
    )
    print(repr(test_prompt))