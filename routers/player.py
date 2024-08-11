from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto import player as dto
from services import player


router = APIRouter()


# Получить список всех игроков
@router.get('/all', tags=['player'])
async def get_players(db: Session = Depends(get_connection)):
    return player.get_players(db)


# Получить игрока по id
@router.get('/{id}', tags=['player'])
async def get_player(id: str = None, db: Session = Depends(get_connection)):
    return player.get_player(db, int(id))


# Удалить игрока по id
@router.delete('/{id}', tags=['player'])
async def delete_player(id: str = None, db: Session = Depends(get_connection)):
    return player.delete_player(db, int(id))


# Обновить игрока по id
@router.put('/{id}', tags=['player'])
async def update_player(id: str = None, db: Session = Depends(get_connection), data: dto.Player = None):
    return player.update_player(db, int(id), data)


# Добавить игрока
@router.post('/', tags=['player'])
async def create_player(db: Session = Depends(get_connection), data: dto.PlayerCreate = None):
    return player.create_new_player(db, data)
