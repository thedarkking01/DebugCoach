import { useState } from "react";
import { analyze } from "./api";
import ProgressBar from "./components/ProgressBar";
import HintCard from "./components/HintCard";
import SolutionCard from "./components/SolutionCard";
import "./App.css";

const LANGUAGES = ["Python", "JavaScript"];

export default function App() {
  const [language, setLanguage] = useState("Python");
  const [code, setCode] = useState("");
  const [error, setError] = useState("");
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [apiError, setApiError] = useState("");

  async function handleAnalyze() {
    if (!code.trim() || !error.trim()) {
      setApiError("Please paste your code and error message.");
      return;
    }
    setApiError("");
    setLoading(true);
    try {
      const data = await analyze({ language, code, error, goal, hint_level: 1 });
      setResult(data);
    } catch {
      setApiError("Could not reach the backend. Is it running?");
    } finally {
      setLoading(false);
    }
  }

  async function handleNext() {
    setLoading(true);
    try {
      const nextLevel = result.hint_level + 1;
      const data = await analyze({ language, code, error, goal, hint_level: nextLevel });
      setResult(data);
    } catch {
      setApiError("Something went wrong. Try again.");
    } finally {
      setLoading(false);
    }
  }

  function handleReset() {
    setResult(null);
    setCode("");
    setError("");
    setGoal("");
    setApiError("");
  }

  return (
    <div className="app">
      <header>
        <h1>🐛 DebugCoach</h1>
        <p className="tagline">Learn to debug. Don't just copy.</p>
      </header>

      {!result ? (
        <div className="form card">
          <label>Language</label>
          <select value={language} onChange={(e) => setLanguage(e.target.value)}>
            {LANGUAGES.map((l) => <option key={l}>{l}</option>)}
          </select>

          <label>Your Code</label>
          <textarea
            className="code-input"
            placeholder="Paste your code here…"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            rows={8}
            spellCheck={false}
          />

          <label>Error Message</label>
          <textarea
            placeholder="Paste the error here…"
            value={error}
            onChange={(e) => setError(e.target.value)}
            rows={3}
            spellCheck={false}
          />

          <label>What were you trying to do? <span className="optional">(optional)</span></label>
          <input
            type="text"
            placeholder="e.g. Print every item in the list"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
          />

          {apiError && <p className="error-msg">{apiError}</p>}

          <button className="btn primary" onClick={handleAnalyze} disabled={loading}>
            {loading ? "Analyzing…" : "💡 Help Me Understand"}
          </button>
        </div>
      ) : (
        <div className="result">
          <ProgressBar hintLevel={result.hint_level} />
          {result.is_final
            ? <SolutionCard data={result} onReset={handleReset} />
            : <HintCard data={result} onNext={handleNext} loading={loading} />
          }
        </div>
      )}
    </div>
  );
}
