export default function QuickActions({ actions = [], onSelect }) {
  if (!actions.length) return null;

  return (
    <div className="flex flex-wrap gap-2 mt-2">
      {actions.map((action, idx) => (
        <button
          key={idx}
          onClick={() => onSelect(action.value)}
          className="
            px-3 py-1.5 rounded-full text-sm
            bg-slate-700 text-slate-100
            hover:bg-slate-600
            transition
          "
        >
          {action.label}
        </button>
      ))}
    </div>
  );
}
