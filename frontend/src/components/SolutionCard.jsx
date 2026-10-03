export default function SolutionCard({ data, onReset }) {
  return (
    <div className="card solution-card">
      <p className="card-label">🎓 Solution</p>
      <span className="concept-badge">{data.concept}</span>

      <div className="section">
        <p className="section-title">What went wrong?</p>
        <p>{data.explanation}</p>
      </div>

      <div className="section">
        <p className="section-title">Your mistake</p>
        <p>{data.mistake}</p>
      </div>

      <div className="section">
        <p className="section-title">Correct approach</p>
        <pre className="code-block">{data.solution}</pre>
      </div>

      <div className="section practice">
        <p className="section-title">🧠 Practice</p>
        <p>{data.practice_question}</p>
      </div>

      <button className="btn" onClick={onReset}>Try Another Problem</button>
    </div>
  );
}
