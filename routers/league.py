from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import league
from dto.league import LeagueDTO
from database import get_connection


router = APIRouter()


@router.get("/all", tags=['league'])
async def get_all_leagues(db: Session = Depends(get_connection)):
    return league.get_all_leagues(db)


@router.get("/{id}", tags=['league'])
async def get_league_by_id(db: Session = Depends(get_connection), id: str = None):
    return league.get_league_by_id(db, int(id))


@router.post("/", tags=['league'])
async def create_league(db: Session = Depends(get_connection), data: LeagueDTO = None):
    return league.create_league(db, data)


@router.delete("/{id}", tags=['league'])
async def delete_league_by_id(db: Session = Depends(get_connection), id: str = None):
    return league.delete_league_by_id(db, int(id))


@router.put("/{id}", tags=['league'])
async def update_league_by_id(db: Session = Depends(get_connection), id: str = None, data: LeagueDTO = None):
    return league.update_league_by_id(db, int(id), data)
