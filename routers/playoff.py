from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_connection
from services import playoff

router = APIRouter()


@router.get("/get_grid", tags=["playoff"])
async def get_grid(db: Session = Depends(get_connection), playoff_id: str = None):
    return playoff.get_the_grid(db, int(playoff_id), 'Финал')