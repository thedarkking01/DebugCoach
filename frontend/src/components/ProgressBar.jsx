export default function ProgressBar({ hintLevel }) {
  const steps = ["Hint 1", "Hint 2", "Hint 3", "Solution"];
  return (
    <div className="progress-bar">
      {steps.map((label, i) => (
        <div key={i} className={`step ${hintLevel > i ? "done" : ""} ${hintLevel === i + 1 ? "active" : ""}`}>
          <div className="dot" />
          <span>{label}</span>
        </div>
      ))}
    </div>
  );
}
