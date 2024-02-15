# Description: This file contains the FastAPI implementation.
from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError, UUID4
from typing import Dict, Optional, Union, List
import uvicorn

app = FastAPI()

# Testing Code to check FastAPI implementation
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    app_module = "main:app"
    uvicorn.run(app_module, host="0.0.0.0", port=8000, reload=True)