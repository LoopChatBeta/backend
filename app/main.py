from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from datetime import datetime, timezone
import uuid

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

class ChatRequest(BaseModel):
    conversation_id: str | None = None
    message: str

@app.get("/")
def root():
    return {"message": "LoopChat API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower()

    conversation_id = (
    	request.conversation_id
    	or f"{uuid.uuid4()}"
    )

    message_id = f"{uuid.uuid4()}"
    timestamp = datetime.now(timezone.utc).isoformat()

    # Appointment workflow
    if any(word in message for word in [
        "appointment",
        "schedule",
        "book",
        "visit"
    ]):
        return {
	    "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "reply": (
                "I'd be happy to help schedule an appointment. "
                "Please provide your name, email, and phone number."
            ),
            "intent": "appointment"
        }

    # Insurance workflow
    if any(word in message for word in [
        "insurance",
        "medicare",
        "aetna",
        "blue cross"
    ]):
        return {
	    "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "reply": (
                "We accept most major insurance plans, including "
                "Medicare, Aetna, and Blue Cross."
            ),
            "intent": "insurance"
        }

    # Office hours workflow
    if any(word in message for word in [
        "hours",
        "open",
        "close"
    ]):
        return {
	    "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "reply": (
                "Our office is open Monday through Friday "
                "from 8:00 AM to 5:00 PM."
            ),
            "intent": "hours"
        }

    # Location workflow
    if any(word in message for word in [
        "address",
        "location",
        "where"
    ]):
        return {
	    "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "reply": (
                "Our clinic is located at "
                "123 Main Street, Anytown, USA."
            ),
            "intent": "location"
        }

    # Default response
    return {
	"conversation_id": conversation_id,
        "message_id": message_id,
        "timestamp": timestamp,
        "reply": (
            "Thank you for contacting our clinic. "
            "How can I help you today?"
        ),
        "intent": "general"
    }
