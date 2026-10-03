from pydantic import BaseModel
from typing import Optional


class AnalyzeRequest(BaseModel):
    language: str
    code: str
    error: str
    goal: Optional[str] = ""
    hint_level: int = 1


class HintResponse(BaseModel):
    hint: str
    question: str
    concept: str
    hint_level: int
    is_final: bool = False


class SolutionResponse(BaseModel):
    concept: str
    explanation: str
    mistake: str
    solution: str
    practice_question: str
    hint_level: int
    is_final: bool = True
