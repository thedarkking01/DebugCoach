HINT_LEVEL_INSTRUCTIONS = {
    1: "Give a very conceptual hint. Do NOT mention specific variable names or line numbers. Point to the general concept only.",
    2: "Be more specific. You may reference the variable or loop involved. Ask a targeted question about the boundary or value.",
    3: "Give an almost-complete hint. The learner should be able to fix it after reading this. You may reference the exact expression causing the issue.",
}


def build_hint_prompt(language: str, code: str, error: str, goal: str, hint_level: int) -> str:
    instruction = HINT_LEVEL_INSTRUCTIONS[hint_level]
    return f"""You are DebugCoach, an AI programming tutor. Help the learner debug WITHOUT giving the solution.

Hint level {hint_level}/3: {instruction}

Language: {language}
Code:
{code}

Error: {error}
Goal: {goal or "Fix the error"}

Respond ONLY with valid JSON, no markdown, no explanation:
{{
  "hint": "<short hint>",
  "question": "<one thinking question>",
  "concept": "<programming concept name>"
}}"""


def build_solution_prompt(language: str, code: str, error: str, goal: str) -> str:
    return f"""You are DebugCoach. The learner has exhausted all hints. Now explain and solve.

Language: {language}
Code:
{code}

Error: {error}
Goal: {goal or "Fix the error"}

Respond ONLY with valid JSON, no markdown, no explanation:
{{
  "concept": "<concept name>",
  "explanation": "<explain why the error happens>",
  "mistake": "<what specifically the learner did wrong>",
  "solution": "<corrected code only>",
  "practice_question": "<one follow-up practice question>"
}}"""
