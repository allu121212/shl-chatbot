from fastapi import FastAPI
from pydantic import BaseModel
class ChatRequest(BaseModel):
    message:str
from agent import generate_response

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    some_response = "Which role are you hiring for?"
    return {"response":some_response}

    messages = [
        {
            "role": m.role,
            "content": m.content
        }
        for m in request.messages
    ]

    return generate_response(messages)
