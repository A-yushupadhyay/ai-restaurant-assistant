import { useContext } from "react";
import { RestaurantContext } from "./RestaurantContext";

export function useRestaurant() {
  return useContext(RestaurantContext);
}
