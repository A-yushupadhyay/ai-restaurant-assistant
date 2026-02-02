from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173" , "https://ai-restaurant-assistant-hs0j.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers AFTER middleware
from app.api.chat import router as chat_router
from app.api.restaurant import router as restaurant_router

app.include_router(chat_router, prefix="/api")
app.include_router(restaurant_router)
