import os
import json
from dotenv import load_dotenv
from google import genai

from backend.prompts import build_hint_prompt, build_solution_prompt
from backend.schemas import HintResponse, SolutionResponse

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.5-flash-lite"


def _call_model(prompt: str) -> dict:
    response = client.models.generate_content(model=MODEL, contents=prompt)
    text = response.text.strip()
    # Strip markdown code fences if model wraps JSON in them
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def generate_hint(language: str, code: str, error: str, goal: str, hint_level: int) -> HintResponse | SolutionResponse:
    if hint_level > 3:
        prompt = build_solution_prompt(language, code, error, goal)
        data = _call_model(prompt)
        return SolutionResponse(**data, hint_level=hint_level, is_final=True)

    prompt = build_hint_prompt(language, code, error, goal, hint_level)
    data = _call_model(prompt)
    return HintResponse(**data, hint_level=hint_level, is_final=False)
