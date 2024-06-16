from fastapi import APIRouter

from app.bookings.schemas import SBooking
from app.bookings.service import BookingService

router = APIRouter(
    prefix='/bookings',
    tags=['bookings']
)
@router.get('')
async def get_all() -> list[SBooking]:
    result = await BookingService.get_all()
    return result

@router.get('/{booking_id}')
async def get_one(booking_id: int) -> SBooking:
    result = await BookingService.get_by_id(booking_id)
    return result

