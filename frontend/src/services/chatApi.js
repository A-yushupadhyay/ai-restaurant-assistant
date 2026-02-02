const API_URL = import.meta.env.VITE_API_URL;

export async function sendMessage({ message, sessionId }) {
  const payload = {
    message,
    session_id: sessionId || null,
  };

  const res = await fetch(`${API_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Failed to send message");
  }

  return res.json();
}
