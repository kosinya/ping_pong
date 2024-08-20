from fastapi import HTTPException

from database import Session
from models.league import League
from models.player import Player
from dto import league as dto


# Получить список всех лиг
def get_all_leagues(db: Session, t_id: int):
    return db.query(League).filter_by(tournament_id=t_id).all()


# Получить лигу по id
def get_league_by_id(db: Session, league_id: int):
    return db.query(League).filter_by(id=league_id).first()


# Создать лигу
def create_league(db: Session, t_id: int, data: dto.LeagueCreate):
    new_league = League(
        name=data.name,
        n_groups=data.n_groups,
        tournament_id=t_id
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
    lg = db.query(League).filter_by(id=league_id).delete()
    db.commit()
    db.refresh()
    return lg


# Обновить лигу по id
def update_league_by_id(db: Session, league_id: int, data: dto.League):
    league = db.query(League).filter_by(id=league_id).first()
    league.name = data.name
    league.n_groups = data.n_groups

    try:
        db.add(league)
        db.commit()
        db.refresh(league)
    except Exception as e:
        db.rollback()
        print(e)

    return league


def add_players(db: Session, league_id: int, player_ids: str):
    new_player_ids = [int(item) for item in player_ids.split(',')]
    ids = [i[0] for i in db.query(Player.id).all()]

    league = db.query(League).filter_by(id=league_id).first()

    for p in new_player_ids:
        if p not in ids:
            raise HTTPException(status_code=404, detail=f'Player with id = {p} not found')

    new_league_players = league.players + ',' + ','.join([str(i) for i in new_player_ids])

    league.players = new_league_players

    try:
        db.add(league)
        db.commit()
        db.refresh(league)
    except Exception as e:
        print(e)
        db.rollback()

    return league
