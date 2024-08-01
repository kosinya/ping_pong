from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto.player import PlayerDTO
from services import player


router = APIRouter()


@router('/all', prefix=['player'])
def get_all_player(db: Session = Depends(get_connection)):
    ...