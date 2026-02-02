export default function DishCard({ name, price, tags, image_url }) {
  return (
    <div className="bg-slate-800 rounded-2xl overflow-hidden shadow-soft
                    hover:scale-[1.02] transition-transform duration-200">
      
      {/* Image / Fallback */}
      {image_url ? (
        <img
          src={image_url}
          alt={name}
          className="h-32 w-full object-cover"
        />
      ) : (
        <div className="h-32 bg-gradient-to-br from-slate-700 to-slate-600
                        flex items-center justify-center text-slate-300">
          <span className="text-3xl">🍽️</span>
        </div>
      )}

      {/* Content */}
      <div className="p-4">
        <div className="flex justify-between items-start gap-2">
          <h3 className="text-white font-semibold leading-tight">
            {name}
          </h3>
          <span className="text-green-400 font-bold whitespace-nowrap">
            ₹{price}
          </span>
        </div>

        {/* Tags */}
        <div className="mt-2 flex flex-wrap gap-2">
          {tags?.map((tag, idx) => (
            <span
              key={idx}
              className="text-xs px-2 py-1 bg-slate-700/80
                         text-slate-200 rounded-full"
            >
              {tag}
            </span>
          ))}
        </div>

        {/* Action */}
        <button
          className="mt-4 w-full text-sm py-2 rounded-xl
                     bg-brand/20 text-brand
                     hover:bg-brand/30 transition"
        >
          Tell me more
        </button>
      </div>
    </div>
  );
}
