import { useState } from "react";

export default function ChatInput({ onSend, disabled }) {
  const [text, setText] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (!text.trim() || disabled) return;

    onSend(text.trim());
    setText("");
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="p-3 bg-slate-900 border-t border-slate-700 flex items-center gap-2"
    >
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Ask naturally… e.g. spicy vegetarian under 250"
        disabled={disabled}
        className="
          flex-1 px-4 py-2 rounded-2xl
          bg-slate-800 text-white placeholder-slate-400
          outline-none transition
          focus:ring-2 focus:ring-brand
        "
      />

      <button
        type="submit"
        disabled={disabled}
        className="
          px-4 py-2 rounded-xl font-medium
          bg-brand text-white
          hover:opacity-90 active:scale-95
          transition disabled:opacity-50
        "
      >
        Send
      </button>
    </form>
  );
}
