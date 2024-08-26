from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import match
from dto import match as dto
from database import get_connection

router = APIRouter()


@router.put('/', tags=['match'])
def update_match_result(db: Session = Depends(get_connection), id: str = None, winner_id: str = None):
    return match.update_match_result(db, int(id), int(winner_id))
