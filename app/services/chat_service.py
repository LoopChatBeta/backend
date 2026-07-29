import uuid

from datetime import datetime, timezone

class ChatService:

    def __init__(self, intent_engine):
        self.intent_engine = intent_engine

    def chat(
        self,
        conversation_id,
        message
    ):

        conversation_id = (
            conversation_id
            or str(uuid.uuid4())
        )

        message_id = str(uuid.uuid4())

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        result = self.intent_engine.respond(
            message
        )

        return {
            "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "intent": result["intent"],
            "reply": result["reply"]
        }
