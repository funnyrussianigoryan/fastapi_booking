from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings
from app.service.base import BaseService


class BookingService(BaseService):
    model = Bookings
