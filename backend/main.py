from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import AnalyzeRequest, HintResponse, SolutionResponse
from backend.ai_service import generate_hint

app = FastAPI(
    title="DebugCoach API",
    description="AI programming tutor that helps learners debug step by step.",
    version="1.0.0"
)

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://debugcoach-frontend.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "DebugCoach API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze", response_model=HintResponse | SolutionResponse)
def analyze(request: AnalyzeRequest):
    if request.hint_level < 1:
        raise HTTPException(status_code=400, detail="hint_level must be >= 1")

    return generate_hint(
        language=request.language,
        code=request.code,
        error=request.error,
        goal=request.goal,
        hint_level=request.hint_level,
    )
