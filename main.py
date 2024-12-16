import os
import openai
from fastapi import FastAPI

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: dict):
    user_message = request.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
        )
        return {"response": response.choices[0].message["content"]}
    except Exception as e:
        return {"detail": f"Ошибка OpenAI: {e}"}