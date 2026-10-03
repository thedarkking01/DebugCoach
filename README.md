# 🐛 DebugCoach

> An AI debugging tutor that helps you fix your code — without immediately giving you the answer.

Most AI tools hand you the solution the moment you paste an error. DebugCoach doesn't. It guides you through **progressive hints** so you actually understand what went wrong.

```
Paste Code + Error
       ↓
   💡 Hint 1  →  think
       ↓
   💡 Hint 2  →  think harder
       ↓
   💡 Hint 3  →  almost there
       ↓
   🎓 Solution + Explanation + Practice Question
```

Built for the [Hacktoberfest Weekend Challenge 2026](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01).

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 19, Vite |
| Backend | Python, FastAPI, Pydantic |
| AI | Open-weight model (Llama 3 / Mistral via Groq) |
| Dev tooling | Amazon Q Developer |

---

## Project Structure

```
DebugCoach/
├── backend/
│   ├── main.py          # FastAPI app, CORS, /analyze endpoint
│   ├── ai_service.py    # Model calls, JSON parsing
│   ├── prompts.py       # Hint level prompts + solution prompt
│   ├── schemas.py       # Pydantic request/response models
│   └── requirements.txt
└── frontend/
    └── src/
        ├── components/
        │   ├── HintCard.jsx
        │   ├── SolutionCard.jsx
        │   └── ProgressBar.jsx
        ├── App.jsx
        ├── api.js
        └── App.css
```

---

## Running Locally

### Prerequisites

- Python 3.10+
- Node.js 18+
- A [Groq API key](https://console.groq.com) (free)

### 1. Clone

```bash
git clone https://github.com/your-username/DebugCoach.git
cd DebugCoach
```

### 2. Backend

```bash
pip install -r backend/requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
```

Start the server:

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173).

---

## API

### `POST /analyze`

**Request**
```json
{
  "language": "python",
  "code": "numbers = [10,20,30]\nfor i in range(len(numbers)):\n    print(numbers[i+1])",
  "error": "IndexError: list index out of range",
  "goal": "Print every item in the list",
  "hint_level": 1
}
```

**Hint response** (`hint_level` 1–3)
```json
{
  "hint": "Think about the largest valid index for this list.",
  "question": "What happens when i reaches the last position?",
  "concept": "Off-by-one error",
  "hint_level": 1,
  "is_final": false
}
```

**Solution response** (`hint_level` 4+)
```json
{
  "concept": "List indexing",
  "explanation": "Python lists are zero-indexed...",
  "mistake": "You accessed numbers[i+1] on the last iteration.",
  "solution": "for i in range(len(numbers)):\n    print(numbers[i])",
  "practice_question": "Can you print every element without using range()?",
  "hint_level": 4,
  "is_final": true
}
```

---

## Why an Open-Weight Model?

The challenge requires open-source/open-weight AI at the core. Here's why it matters for DebugCoach specifically:

- **Privacy** — learner code (which may contain personal projects or work code) never has to go to a proprietary closed API
- **Swappable** — the model can be changed in one file (`ai_service.py`) without touching anything else
- **Self-hostable** — you can run the same model locally via Ollama, keeping everything on your machine
- **No vendor lock-in** — the hint engine logic is independent of which model powers it

---

## Supported Languages

- Python
- JavaScript

---

## License

MIT
