import { useRestaurant } from "../context/useRestaurant";

export default function RestaurantHeader() {
  const restaurant = useRestaurant();

  return (
    <div className="relative h-44 overflow-hidden">
      <img
        src={restaurant.heroImage}
        alt={restaurant.name}
        className="absolute inset-0 w-full h-full object-cover"
      />

      {/* Dark gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent" />

      <div className="relative z-10 h-full flex flex-col justify-end p-4">
        <h1 className="text-white text-2xl font-semibold tracking-tight">
          {restaurant.name}
        </h1>
        <p className="text-slate-300 text-sm mt-1">
          {restaurant.cuisine}
        </p>

        <div className="flex items-center gap-2 mt-2">
          <span className="text-xs px-2 py-1 bg-green-500/20 text-green-300 rounded-full">
            Open Now
          </span>
          <span className="text-xs px-2 py-1 bg-white/10 text-white rounded-full">
            AI Assistant Available
          </span>
        </div>
      </div>
    </div>
  );
}
