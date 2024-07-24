from sqlalchemy.orm import Session
from dto.tournament import TournamentDTO
from models.tournament import Tournament


# Получить список всех турниров
def get_all_tournaments(db: Session):
    return db.query(Tournament).all()


# Получить турнир по id
def get_tournament_by_id(db: Session, tournament_id: int):
    return db.query(Tournament).filter_by(id=tournament_id).first()


# Получить турнир по имени
def get_tournament_by_name(db: Session, tournament_name: str):
    return db.query(Tournament).filter_by(name=tournament_name).first()


# Создать турнир
def create_tournament(db: Session, data: TournamentDTO):
    new_tournament = Tournament(name=data.name)

    try:
        db.add(new_tournament)
        db.commit()
        db.refresh(new_tournament)
    except Exception as e:
        print(e)
        db.rollback()

    return new_tournament


# Удалить турнир
def delete_tournament(db: Session, tournament_id: int):
    tm = -1
    try:
        tm = db.query(Tournament).filter_by(id=tournament_id).delete()
        db.commit()
        db.refresh(Tournament)
    except Exception as e:
        print(e)
        db.rollback()

    return tm
