const API_URL = "http://localhost:8000/api/chat";

export async function sendMessage({ message, sessionId }) {
  const payload = {
    message,
    session_id: sessionId || null,
  };

  const res = await fetch(API_URL, {
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
