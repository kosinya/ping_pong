from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_connection
from services import tournament
from dto.tournament import TournamentDTO


router = APIRouter()


@router.get("/all", tags=['tournament'])
async def get_tournament(db: Session = Depends(get_connection)):
    return tournament.get_all_tournaments(db)


@router.get('/{id}', tags=['tournament'])
async def get_tournament_by_id(id: str = None, db: Session = Depends(get_connection)):
    return tournament.get_tournament_by_id(db, int(id))


@router.delete('/{id}', tags=['tournament'])
async def delete_tournament_by_id(id: str = None, db: Session = Depends(get_connection)):
    return tournament.delete_tournament(db, int(id))


@router.put('/{id}', tags=['tournament'])
async def update_tournament_status_by_id(data: TournamentDTO, id: str = None, db: Session = Depends(get_connection)):
    return tournament.update_tournament(db, int(id), data)


@router.post('/', tags=['tournament'])
async def create_tournament(db: Session = Depends(get_connection), data: TournamentDTO = None):
    return tournament.create_tournament(db, data)
