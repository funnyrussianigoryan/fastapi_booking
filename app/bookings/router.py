from fastapi import APIRouter, Depends

from app.bookings.schemas import SBooking
from app.bookings.service import BookingService
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['bookings']
)
@router.get('')
async def get_all(user: Users=Depends(get_current_user)) -> list[SBooking]:
    result = await BookingService.get_all(user_id=user.id)
    return result

'''@router.get('/{booking_id}')
async def get_one(booking_id: int) -> SBooking:
    result = await BookingService.get_by_id(booking_id)
    return result'''

