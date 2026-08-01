import uuid

from datetime import datetime, timezone

class ChatService:

    def __init__(self, intent_engine, llm):
        self.intent_engine = intent_engine
        self.llm = llm

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

        if result["intent"] != "general":
            return {
                "conversation_id": conversation_id,
                "message_id": message_id,
                "timestamp": timestamp,
                "intent": result["intent"],
                "reply": result["reply"]
            }

        reply = self.llm.chat(
            system_prompt="""
            You are a clinic assistant.
            """,
            user_message=message
        )

        return {
            "conversation_id": conversation_id,
            "message_id": message_id,
            "timestamp": timestamp,
            "intent": "llm",
            "reply": reply
        }

