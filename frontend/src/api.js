const BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function analyze({ language, code, error, goal, hint_level }) {
  const res = await fetch(`${BASE}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language, code, error, goal, hint_level }),
  });
  if (!res.ok) throw new Error("API error");
  return res.json();
}
