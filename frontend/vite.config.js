import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "https://ai-restaurant-assistant-hs0j.onrender.com",
        changeOrigin: true,
        secure: false,
      },
      "/restaurant": {
        target: "https://ai-restaurant-assistant-hs0j.onrender.com",
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
