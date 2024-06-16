from fastapi import FastAPI
from app.bookings.router import router as hotels

app = FastAPI()

app.include_router(hotels)
