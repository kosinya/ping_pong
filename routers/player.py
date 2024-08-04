from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto.player import PlayerDTO
from services import player


router = APIRouter()


@router('/men', prefix=['player'])
async def get_all_men(db: Session = Depends(get_connection)):
    return player.get_all_men(db)


@router('/women', prefix=['player'])
async def get_all_women(db: Session = Depends(get_connection)):
    return player.get_all_women(db)


@router('/{id}', prefix=['player'])
async def get_player_by_id(id: str, db: Session = Depends(get_connection)):
    return player.get_player_by_id(db, int(id))


@router('/{id}', prefix=['player'])
async def delete_player_by_id(id: str, db: Session = Depends(get_connection)):
    return player.delete_player_by_id(db, int(id))


@router('/{id}', prefix=['player'])
async def update_player_by_id(id: str, db: Session = Depends(get_connection), data: PlayerDTO = None):
    return player.update_player_by_id(db, int(id), data)
