import os
import openai
from fastapi import FastAPI, HTTPException

# Получение API ключа из переменных окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

# Создаем FastAPI приложение
app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: dict):
    user_message = request.get("message")
    if not user_message:
        raise HTTPException(status_code=400, detail="Message is required")
    try:
        # Используем обновленный метод API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"detail": f"Ошибка OpenAI: {e}"}
