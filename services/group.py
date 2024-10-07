import itertools
from sqlalchemy import text

from models.group import Group
from models.match import Match
from dto import group
from database import Session


def add_player_to_group(db: Session, data: group.GroupCreate, league_id: int):
    new = Group(
        player_id=data.player_id,
        score=data.score,
        group_name=data.group_name,
        league_id=league_id
    )

    try:
        db.add(new)
        db.commit()
        db.refresh(new)
    except Exception as e:
        print(e)
        db.rollback()

    return new


def get_all_groups(db: Session, l_id: int):
    query = text(f"""SELECT g.*, p.surname, p.name, p.patronymic
                     FROM groups g
                     JOIN players p ON g.player_id = p.player_id
                     WHERE g.league_id = {l_id}
                     ORDER BY g.group_name ASC;""")
    results = db.execute(query).fetchall()

    data = []
    if results:
        for r in results:
            data.append({
                "id": r[0],
                "player_id": r[1],
                "score": r[2],
                "place": r[3],
                "group_name": r[4],
                "league_id": r[5],
                "surname": r[6],
                "name": r[7],
                "patronymic": r[8]
            })
    return data


def updating_the_results(db: Session, league_id: int, group_name: str):
    g = db.query(Group).filter_by(league_id=league_id, group_name=group_name).all()
    ranked = rank_players(g, 1)

    ranked_players = {}
    for player in ranked:
        if player.place not in ranked_players:
            ranked_players[player.place] = []
        ranked_players[player.place].append(player)

    for rank, players_in_rank in ranked_players.items():
        ids = []
        if len(players_in_rank) > 1:
            for player in players_in_rank:
                ids.append(player.player_id)
            pairs = itertools.combinations(ids, 2)
            matches = db.query(Match)
        print(ids)

    db.add_all(ranked)
    db.commit()
    return ranked


def rank_players(players, r):
    players.sort(key=lambda x: x.score, reverse=True)

    current_rank = r
    previous_score = players[0].score

    for i, player in enumerate(players):
        if player.score != previous_score:
            current_rank = current_rank + 1
        previous_score = player.score
        player.place = current_rank

    return players
