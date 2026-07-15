from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
app = FastAPI()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


class QuizRequest(BaseModel):
    topic: str
    difficulty: str
    questions: int


@app.post("/generate_quiz")
def generate_quiz(data: QuizRequest):

    prompt = f"""
    Generate {data.questions} multiple choice questions.

    Topic: {data.topic}
    Difficulty: {data.difficulty}

    Format:

    Question:
    A.
    B.
    C.
    D.
    Answer:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "quiz": response.text
    }