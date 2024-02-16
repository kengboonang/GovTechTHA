from pydantic import BaseModel, conint, constr, Field
from typing import Optional, Union

class Request(BaseModel):
    """
    Request details associated with the error
    """
    
class Details(BaseModel):
    """
    Other details associated with the error
    """

class APIError(BaseModel):
    """
    Generic schema for expressing API errors
    """
    code: conint(ge=400, le=600) = Field(..., description="API Error code associated with the error")
    message: constr() = Field(..., description="API Error message associated with the error")
    request: Optional[Request] = Field(default=None, description="Request details associated with the error")
    details: Optional[Details] = Field(default=None, description="Other details associated with the error")

if __name__ == "__main__":
    # test APIError class
    test_error = APIError(
        code=404,
        message="Resource not found"
    )
    print(repr(test_error))