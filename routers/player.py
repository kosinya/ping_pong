from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto.player import PlayerDTO
from services import player


router = APIRouter()


# Получить список всех мужчин
@router.get('/men', tags=['player'])
async def get_all_men(db: Session = Depends(get_connection)):
    return player.get_all_men(db)


# Получить список всех женшин
@router.get('/women', tags=['player'])
async def get_all_women(db: Session = Depends(get_connection)):
    return player.get_all_women(db)


# Получить игрока по id
@router.get('/{id}', tags=['player'])
async def get_player_by_id(id: str = None, db: Session = Depends(get_connection)):
    return player.get_player_by_id(db, int(id))


# Удалить игрока по id
@router.delete('/{id}', tags=['player'])
async def delete_player_by_id(id: str = None, db: Session = Depends(get_connection)):
    return player.delete_player_by_id(db, int(id))


# Обновить игрока по id
@router.put('/{id}', tags=['player'])
async def update_player_by_id(id: str = None, db: Session = Depends(get_connection), data: PlayerDTO = None):
    return player.update_player_by_id(db, int(id), data)


# Добавить игрока
@router.post('/', tags=['player'])
async def create_player(data: PlayerDTO = None, db: Session = Depends(get_connection)):
    return player.create_new_player(db, data)
