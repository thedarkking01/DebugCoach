export default function HintCard({ data, onNext, loading }) {
  const isLast = data.hint_level === 3;
  return (
    <div className="card hint-card">
      <p className="card-label">💡 Hint {data.hint_level}</p>
      <p className="hint-text">{data.hint}</p>
      <p className="question-text">🤔 {data.question}</p>
      <span className="concept-badge">{data.concept}</span>
      <button className="btn" onClick={onNext} disabled={loading}>
        {loading ? "Thinking…" : isLast ? "Show Me the Solution" : "I Still Need Help"}
      </button>
    </div>
  );
}
