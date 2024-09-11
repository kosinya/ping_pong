from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import match
from dto import match as dto
from database import get_connection

router = APIRouter()


@router.get('/all_group_matches', tags=['match'])
def get_all_group_matches(db: Session = Depends(get_connection), league_id: str = None):
    return match.get_group_matches(db, int(league_id))


@router.get('/', tags=['match'])
def get_matches_by_playoff(db: Session = Depends(get_connection), playoff_id: str = None):
    return match.get_matches_by_playoff(db, int(playoff_id))


@router.put('/', tags=['match'])
def update_match_result(db: Session = Depends(get_connection), id: str = None, winner_id: str = None):
    return match.update_match_result(db, int(id), int(winner_id))
