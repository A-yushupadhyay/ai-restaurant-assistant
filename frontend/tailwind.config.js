/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: "#0ea5e9",
        surface: "#0f172a",
      },
      boxShadow: {
        soft: "0 10px 30px rgba(0,0,0,0.15)",
      },
    },
  },
  plugins: [],
};
