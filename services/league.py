import random
from fastapi import HTTPException

from database import Session
from models.league import League
from models.player import Player
from dto import league as leagueDTO
from dto import group as groupDTO
from . import group as groupService


# Получить список всех лиг
def get_all_leagues(db: Session, t_id: int):
    return db.query(League).filter_by(tournament_id=t_id).all()


# Получить лигу по id
def get_league_by_id(db: Session, league_id: int):
    return db.query(League).filter_by(id=league_id).first()


# Создать лигу
def create_league(db: Session, t_id: int, data: leagueDTO.LeagueCreate):
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
def update_league_by_id(db: Session, league_id: int, data: leagueDTO.League):
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


def delete_player(db: Session, league_id: int, player_id: int):
    league = db.query(League).filter_by(id=league_id).first()
    league_players = league.players.split(',')
    print(league_players)

    ids = [i[0] for i in db.query(Player.id).all()]
    if player_id not in ids:
        raise HTTPException(status_code=404, detail=f'Player with id = {player_id} not found')

    if str(player_id) not in league_players:
        raise HTTPException(status_code=404, detail=f'Player with id = {player_id} not found '
                                                    f'in the list of current league players ')

    league_players.remove(str(player_id))
    league.players = ','.join(league_players)
    print(league_players)

    try:
        db.add(league)
        db.commit()
        db.refresh(league)
    except Exception as e:
        print(e)
        db.rollback()

    return league


def draw(db: Session, league_id: int):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    league = db.query(League).filter_by(id=league_id).first()
    ids = [int(i) for i in league.players.split(',')]

    if len(ids) % 4 != 0:
        raise HTTPException(status_code=412, detail=f'The number of players must be a multiple of 4')

    players = db.query(Player).filter(Player.id.in_(ids)).order_by(Player.rating.desc()).all()

    n_iter = len(ids) // 4
    for i in range(n_iter):
        choices = letters[0:league.n_groups-1]
        for j in range(league.n_groups):
            group_name = random.choice(choices)
            choices.remove(group_name)

            player = players[0]
            players.remove(player)

            data = groupDTO.GroupCreate(
                player_id=player.id,
                group_name=group_name,
                score=0
            )

            groupService.add_player_to_group(db, data, league_id)

    return "Успешный успех!"