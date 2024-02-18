from fastapi import APIRouter, HTTPException , Response, status
from pydantic import BaseModel, validator
from typing import Optional

from schemas.queries_schema import Prompt, Role
from chatgpt import ChatGPT

router = APIRouter()

@router.post("/queries/{id}", status_code=status.HTTP_201_CREATED, response_model=Prompt, summary="Create a new query", description="This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised.")
def create_query(id: int, prompt: Optional[Prompt] = None):
    chat = ChatGPT()
    response = chat.generate(prompt.role, prompt.content) if prompt else None
    return {"id": id, "response": response}