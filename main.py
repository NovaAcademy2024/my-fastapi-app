from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

# Создаем FastAPI приложение
app = FastAPI()

# Настройка API ключа
openai.api_key = os.getenv("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")

# Модель данных для запроса
class ChatRequest(BaseModel):
    message: str

# Маршрут для чата
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Убедитесь, что этот модельный идентификатор доступен
            messages=[
                {"role": "user", "content": request.message}
            ]
        )
        # Извлекаем ответ из ответа OpenAI
        return {"response": response.choices[0].message.content}
    except openai.OpenAIError as e:
        # Обработка ошибок OpenAI API
        raise HTTPException(status_code=500, detail=f"Ошибка OpenAI: {e}")
