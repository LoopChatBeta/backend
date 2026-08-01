import os

from openai import OpenAI

from app.interfaces.llm import LLMProvider

class QwenLLM(LLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "DASHSCOPE_API_KEY"
            ),
            base_url=os.getenv(
                "QWEN_BASE_URL"
            )
        )

        self.model = os.getenv(
            "QWEN_MODEL",
            "qwen-plus"
        )

    def chat(
        self,
        system_prompt,
        user_message,
        history=[]
    ):

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(history)

        messages.append({
            "role": "user",
            "content": user_message
        })

        response = (
            self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )
