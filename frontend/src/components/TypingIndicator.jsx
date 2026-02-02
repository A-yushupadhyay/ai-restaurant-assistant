export default function TypingIndicator() {
  return (
    <div className="flex items-center gap-2 px-3 py-1 text-slate-400 text-sm animate-fade-slide">
      <div className="flex gap-1">
        <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" />
        <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-150" />
        <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-300" />
      </div>
      <span>Assistant is typing</span>
    </div>
  );
}
