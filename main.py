import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Чтение ключа API из переменных окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Привет, Render!"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Новый метод OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты дружелюбный помощник."},
                {"role": "user", "content": request.message}
            ]
        )
        # Получение ответа
        return {"response": response.choices[0].message.content}
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка OpenAI: {str(e)}")
