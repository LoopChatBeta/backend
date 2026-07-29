from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from datetime import datetime, timezone
import uuid
import logging

from app.models.chat import ChatRequest
from app.intent.rules import RulesIntentEngine
from app.services.chat_service import ChatService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("loopchat")

app = FastAPI(title="LoopChat API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

intent_engine = RulesIntentEngine()
chat_service = ChatService(intent_engine)

@app.get("/")
def root():
    return {"message": "LoopChat API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(
    chat_request: ChatRequest,
    http_request: Request
):

    client_ip = (
        http_request.client.host
        if http_request.client
        else "unknown"
    )

    result = chat_service.chat(
        chat_request.conversation_id,
        chat_request.message
    )

    logger.info(
        f"conversation_id={result['conversation_id']} "
        f"client_ip={client_ip}"
    )

    return result
