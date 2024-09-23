import os
import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
