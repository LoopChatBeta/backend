from .base import IntentEngine

class RulesIntentEngine(IntentEngine):

    def respond(self, message: str):

        message = message.lower()

        if any(word in message for word in [
            "appointment",
            "schedule",
            "book",
            "visit"
        ]):
            return {
                "intent": "appointment",
                "reply": (
                    "I'd be happy to help schedule an appointment. "
                    "Please provide your name, email, and phone number."
                )
            }

        if any(word in message for word in [
            "insurance",
            "medicare",
            "aetna",
            "blue cross"
        ]):
            return {
                "intent": "insurance",
                "reply": (
                    "We accept most major insurance plans."
                )
            }

        if any(word in message for word in [
            "hours",
            "open",
            "close"
        ]):
            return {
                "intent": "hours",
                "reply": (
                    "Our office is open Monday through Friday "
                    "from 8:00 AM to 5:00 PM."
                )
            }

        if any(word in message for word in [
            "address",
            "location",
            "where"
        ]):
            return {
                "intent": "location",
                "reply": (
                    "Our clinic is located at "
                    "123 Main Street, Anytown, USA."
                )
            }

        return {
            "intent": "general",
            "reply": (
                "Thank you for contacting our clinic. "
                "How can I help you today?"
            )
        }
