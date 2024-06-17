from fastapi import FastAPI

from app.bookings.router import router as hotels
from app.users.router import router as users

app = FastAPI()

app.include_router(users)
app.include_router(hotels)
