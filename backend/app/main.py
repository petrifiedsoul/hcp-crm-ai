from fastapi import FastAPI
from app.routes import chat

app = FastAPI()

app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)