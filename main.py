from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Allows requests from these origins
    allow_credentials=True,         # Allows cookies and authentication headers
    allow_methods=["*"],            # Allows all standard HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # Allows all custom and standard HTTP headers
)

class PromptRequest(BaseModel):
    prompt:str

@app.post("/generate")
def generate(request: PromptRequest):
    response=model.generate_content(request.prompt)
    return {"response": response.text}

