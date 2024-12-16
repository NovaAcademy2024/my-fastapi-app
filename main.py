from fastapi import FastAPI, Request
import openai

app = FastAPI()

# Приветствие на главной странице
@app.get("/")
def read_root():
    return {"message": "Привет, Render!"}

# Обработчик чата
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Ответ с использованием OpenAI API
    try:
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = response['choices'][0]['message']['content']
        return {"response": bot_response}

    except Exception as e:
        return {"error": str(e)}
