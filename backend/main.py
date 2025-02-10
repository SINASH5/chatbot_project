from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from services.chat_service import generate_response  # ✅ Corrected import
from services.llm_service import generate_llm_response  # ✅ Corrected import

app = FastAPI()

# Define input model
class UserInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(user_input: UserInput):
    try:
        # First, check if a predefined response exists
        bot_response = generate_response(user_input.message)

        # If no predefined response, use LLM
        if bot_response == "I'm not sure how to respond to that.":
            bot_response = generate_llm_response(user_input.message)

        return JSONResponse(content={"response": bot_response}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
def home():
    return {"message": "FastAPI Chatbot is running!"}
