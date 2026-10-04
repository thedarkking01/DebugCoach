import os
import json
from dotenv import load_dotenv
from groq import Groq

from backend.prompts import build_hint_prompt, build_solution_prompt
from backend.schemas import HintResponse, SolutionResponse

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)
MODEL = "qwen/qwen3.8-27b"


def _call_model(prompt: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    text = response.choices[0].message.content.strip()
    # Strip Qwen3 thinking block if present
    if "</think>" in text:
        text = text.split("</think>")[-1].strip()
    # Strip markdown code fences
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
