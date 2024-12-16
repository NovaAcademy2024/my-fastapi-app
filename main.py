import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Создаем приложение FastAPI
app = FastAPI()

# Загружаем API-ключ из переменной окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

# Модель данных для входящих сообщений
class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    try:
        # Запрос к OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.message}
            ]
        )
        # Возвращаем ответ
        return {"response": response.choices[0].message.content}
    except Exception as e:
        # Обрабатываем ошибки и возвращаем их
        raise HTTPException(status_code=500, detail=f"Ошибка OpenAI: {str(e)}")
