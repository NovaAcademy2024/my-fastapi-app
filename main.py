import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Инициализация FastAPI
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ваш API-ключ OpenAI (убедитесь, что он корректно установлен)
openai.api_key = "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"

# Модель запроса
class ChatRequest(BaseModel):
    message: str

# Маршрут для чата
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Вызов OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Убедитесь, что модель указана корректно
            messages=[
                {"role": "system", "content": "Ты полезный ассистент."},
                {"role": "user", "content": request.message},
            ],
        )
        # Возвращаем ответ
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка OpenAI: {str(e)}")


# Тестовый маршрут
@app.get("/")
def root():
    return {"message": "Привет, Render!"}
