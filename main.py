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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": response['choices'][0]['message']['content']}
    except Exception as e:
        print(f"Ошибка OpenAI: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка OpenAI: {e}")
