import random
from fastapi import HTTPException
import itertools

from database import Session
from models.league import League
from models.player import Player
from models.group import Group
from dto import league as league_dto
from dto import group as group_dto
from dto import match as match_dto
from . import group as group_service
from . import match as match_service

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Получить список всех лиг турнира
def get_all_leagues(db: Session, t_id: int):
    return db.query(League).filter_by(tournament_id=t_id).all()


# Получить лигу по id
def get_league_by_id(db: Session, league_id: int):
    return db.query(League).filter_by(id=league_id).first()


# Создать лигу
def create_league(db: Session, t_id: int, data: league_dto.LeagueCreate):
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
def delete_league(db: Session, league_id: int):
    lg = db.query(League).filter_by(league_id=league_id).delete()
    db.commit()
    return lg


# Обновить лигу по id
def update_league(db: Session, league_id: int, data: league_dto.League):
    league = db.query(League).filter_by(league_id=league_id).first()
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


# Добавить в лигу игроков
def add_players(db: Session, league_id: int, player_ids: str):
    new_player_ids = [int(item) for item in player_ids.split(',')]
    ids = [i[0] for i in db.query(Player.player_id).all()]

    league = db.query(League).filter_by(league_id=league_id).first()

    for p in new_player_ids:
        if p not in ids:
            raise HTTPException(status_code=404, detail=f'Player with id = {p} not found')

    if league.players == "":
        league.players = ','.join([str(i) for i in new_player_ids])
    else:
        league.players = league.players + ',' + ','.join([str(i) for i in new_player_ids])

    try:
        db.add(league)
        db.commit()
        db.refresh(league)
    except Exception as e:
        print(e)
        db.rollback()

    return league


# Удалить игрока из лиги
def delete_player(db: Session, league_id: int, player_id: int):
    league = db.query(League).filter_by(league_id=league_id).first()
    league_players = league.players.split(',')
    print(league_players)

    ids = [i[0] for i in db.query(Player.player_id).all()]
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


# Провести жеребьевку
def draw(db: Session, league_id: int):
    league = db.query(League).filter_by(league_id=league_id).first()
    ids = [int(i) for i in league.players.split(',')]

    if len(ids) % league.n_groups != 0:
        raise HTTPException(status_code=400, detail=f'The number of players must be a multiple of 4')

    players = db.query(Player).filter(Player.player_id.in_(ids)).order_by(Player.rating.desc()).all()

    n_iter = len(ids) // 4
    for i in range(n_iter):
        choices = LETTERS[0:league.n_groups]
        for j in range(league.n_groups):
            group_name = random.choice(choices)
            choices.remove(group_name)

            player = players[0]
            players.remove(player)

            data = group_dto.GroupCreate(
                player_id=player.player_id,
                group_name=group_name,
                score=0
            )

            group_service.add_player_to_group(db, data, league_id)

    groups = db.query(Group).filter_by(league_id=league_id).all()
    create_group_matches(db, league.league_id, groups, league.n_groups)

    return "success"


# Создание групповых матчей
def create_group_matches(db: Session, league_id: int, groups: list, n_groups: int):
    for i in range(n_groups):
        group = [g for g in groups if g.group_name == LETTERS[i]]
        for p1, p2 in itertools.combinations(group, 2):
            match = match_dto.MatchCreate(
                player1_id=p1.id,
                player2_id=p2.id,
                type="Групповой",
                score="",
                group_name=LETTERS[i],
                league_id=league_id,
            )

            match_service.create_match(db, match)


# def complete_the_group_stage(db: Session, league_id: int):
#     n = match_service.get_count_unplayed_group_matches(db, league_id)
#     league = get_league_by_id(db, league_id)
#
#     if n != 0:
#         raise HTTPException(status_code=400, detail=f"{n} more matches have not been played in the group stage")
#
#     groups = group_service.get_all_groups(db, league_id)
#     n = len(groups) // league.n_groups
#     if n > 3:
#         n = 3
#
#     types_of_playoff = ['gold', 'silver', 'bronze']
#     for i in range(n):
#         playoff_player_ids = []
#         for j in range(0, len(groups), 4):
#             playoff_player_ids.append(groups[j+i].player_id)
#         for p in range(0, len(playoff_player_ids), 2):
#             data = match_dto.MatchCreate(
#                 player1_id=playoff_player_ids[p],
#                 player2_id=playoff_player_ids[p+1],
#             )
