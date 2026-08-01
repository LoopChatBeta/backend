from app.interfaces.llm import LLMProvider

class MockLLM(LLMProvider):

    def chat(
        self,
        system_prompt,
        user_message,
        history=[]
    ):

        message = user_message.lower()

        if "appointment" in message:
            return (
                "I'd be happy to help schedule an appointment. "
                "Please provide your name, email, and phone number."
            )

        if "insurance" in message:
            return (
                "We accept most major insurance plans."
            )

        if "hours" in message:
            return (
                "Our office is open Monday through Friday "
                "from 8 AM to 5 PM."
            )

        return (
            "Thank you for contacting our clinic. "
            "How can I help you today?"
        )

