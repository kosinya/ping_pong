from database import Session
from models.league import League
from dto.league import LeagueDTO


# Получить список всех лиг
def get_all_leagues(db: Session):
    return db.query(League).all()


# Получить лигу по id
def get_league_by_id(db: Session, league_id: int):
    return db.query(League).filter_by(id=league_id).first()


# Создать лигу
def create_league(db: Session, data: LeagueDTO):
    new_league = League(
        name=data.name,
        n_groups=data.n_groups,
        tournament_id=data.tournament_id
    )
    try:
        db.add(new_league)
        db.commit()
        db.refresh(new_league)
    except Exception as e:
        db.rollback()
        print(e)

    return new_league


# Удалить лигу по id
def delete_league_by_id(db: Session, league_id: int):
    db.query(League).filter_by(id=league_id).delete()
    db.commit()
    db.refresh(league)
    return league_id


# Обновить лигу по id
def update_league_by_id(db: Session, league_id: int, data: LeagueDTO):
    league = db.query(League).filter_by(id=league_id).first()
    league.name = data.name
    league.n_groups = data.n_groups
    league.tournament_id = data.tournament_id

    try:
        db.add(league)
        db.commit()
        db.refresh(league)
    except Exception as e:
        db.rollback()
        print(e)

    return league
