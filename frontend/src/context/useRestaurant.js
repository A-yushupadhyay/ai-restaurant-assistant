import { useContext } from "react";
import { RestaurantContext } from "./RestaurantContext.js";

export function useRestaurant() {
  return useContext(RestaurantContext);
}
