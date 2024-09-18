from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto import group as dto
from services import group

router = APIRouter()


@router.get('', tags=['group'])
async def get_groups(db: Session = Depends(get_connection), l_id: str = None):
    return group.get_all_groups(db, int(l_id))

