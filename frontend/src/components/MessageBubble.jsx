export default function MessageBubble({ sender, text }) {
  const isUser = sender === "user";

  return (
    <div
      className={`flex ${isUser ? "justify-end" : "justify-start"} animate-slide`}
    >
      <div
        className={`
          max-w-[80%] px-4 py-2 text-sm leading-relaxed rounded-2xl
          shadow-soft backdrop-blur
          ${isUser
            ? "bg-brand text-white rounded-br-sm"
            : "bg-slate-700/80 text-slate-100 rounded-bl-sm"}
        `}
      >
        {text}
      </div>
    </div>
  );
}
