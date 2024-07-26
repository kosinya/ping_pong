from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_connection
from services import tournament
from dto.tournament import TournamentDTO


router = APIRouter()

@router.get("/", )