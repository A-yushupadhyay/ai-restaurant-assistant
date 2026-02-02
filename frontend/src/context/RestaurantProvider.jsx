import { RestaurantContext } from "./RestaurantContext";

export function RestaurantProvider({ children }) {
  const restaurant = {
    id: "spice-garden-001",
    name: "Spice Garden",
    cuisine: "North Indian • Chinese",
    accent: "#22c55e",
    heroImage:
      "https://images.unsplash.com/photo-1600891964599-f61ba0e24092",
  };

  return (
    <RestaurantContext.Provider value={restaurant}>
      {children}
    </RestaurantContext.Provider>
  );
}
