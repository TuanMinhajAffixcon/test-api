from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Define the model for input data using Pydantic
class UserData(BaseModel):
    first_name: str
    middle_name: Optional[str]
    sur_name: str
    dob: str
    address_line1: str
    suburb: str
    state: str
    postcode: str
    mobile: str
    email: str

# API endpoint to accept and return the input data
@app.post("/verify/")
async def verify_user(data: UserData):
    # Simply return the input data as a JSON response
    return {
        "first_name": data.first_name,
        "middle_name": data.middle_name,
        "sur_name": data.sur_name,
        "dob": data.dob,
        "address_line1": data.address_line1,
        "suburb": data.suburb,
        "state": data.state,
        "postcode": data.postcode,
        "mobile": data.mobile,
        "email": data.email
    }

# Default root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the User Verification API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
