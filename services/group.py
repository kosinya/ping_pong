from models.group import Group
from dto.group import Group as dto
from database import Session


def create_group(db: Session, data: dto):
    ...
