from enum import Enum
from pydantic import BaseModel, validator


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

if __name__ == "__main__":
    # test Prompt class
    test_prompt = Prompt(
        role=Role.system, 
        content="Hello, World!"
    )
    print(repr(test_prompt))