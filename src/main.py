# Description: This file contains the FastAPI implementation.
from fastapi import APIRouter, FastAPI, Response, status
import uvicorn

from routers import queries_router

api_router = APIRouter()
app = FastAPI()

# Testing Code to check FastAPI implementation
@api_router.get("/")
def get_root():
    return {"message": "Hello World!"}

app.include_router(queries_router.router)

if __name__ == "__main__":
    app_module = "main:app"
    uvicorn.run(app_module, host="0.0.0.0", port=8000, reload=True)