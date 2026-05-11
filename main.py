from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from agent import chat_agent

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    messages = [m.dict() for m in request.messages]

    response = chat_agent(messages)

    return response