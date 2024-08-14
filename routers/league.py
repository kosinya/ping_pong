from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import league
from dto import league as dto
from database import get_connection


router = APIRouter()


@router.get("/all", tags=['league'])
async def get_all_leagues(db: Session = Depends(get_connection), t_id: str = None):
    return league.get_all_leagues(db, int(t_id))


@router.get("/{id}", tags=['league'])
async def get_league_by_id(db: Session = Depends(get_connection), id: str = None):
    return league.get_league_by_id(db, int(id))


@router.post("/", tags=['league'])
async def create_league(db: Session = Depends(get_connection), data: dto.LeagueCreate = None):
    return league.create_league(db, data)


@router.delete("/{id}", tags=['league'])
async def delete_league_by_id(db: Session = Depends(get_connection), id: str = None):
    return league.delete_league_by_id(db, int(id))


@router.put("/{id}", tags=['league'])
async def update_league_by_id(db: Session = Depends(get_connection), id: str = None, data: dto.League = None):
    return league.update_league_by_id(db, int(id), data)
