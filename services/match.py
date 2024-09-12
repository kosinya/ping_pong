from fastapi.exceptions import HTTPException

from database import Session
from models.match import Match
from models.group import Group
from models.player import Player
from dto import match


def create_match(db: Session, data: match.MatchCreate):
    new_match = Match(
        player1_id=data.player1_id,
        player2_id=data.player2_id,
        type=data.type,
        group_name=data.group_name,
        playoff_id=data.playoff_id,
        league_id=data.league_id
    )

    try:
        db.add(new_match)
        db.commit()
        db.refresh(new_match)
    except Exception as e:
        print(e)
        db.rollback()

    return new_match


def get_group_matches(db: Session, league_id: int):
    q = db.query(Match, Player).join(Player, Match.player1_id == Player.id)
    result = q.filter(Match.league_id == league_id).all()
    return result


def get_matches_by_playoff(db: Session, playoff_id: int):
    return db.query(Match).filter_by(playoff_id=playoff_id).all()


def get_count_unplayed_group_matches(db: Session, league_id: int):
    return db.query(Match).filter_by(league_id=league_id, winner_id=None).count()


def update_match_result(db: Session, mathc_id: int, winner_id: int):
    m = db.query(Match).filter_by(id=mathc_id).first()
    m.winner_id = winner_id
    try:
        db.add(m)
        db.commit()
        db.refresh(m)
    except Exception as e:
        print(e)
        db.rollback()

    if m.type == "Групповой":
        p = db.query(Group).filter_by(league_id=m.league_id, player_id=winner_id).first()
        p.score += 2
        try:
            db.add(p)
            db.commit()
            db.refresh(p)
        except Exception as e:
            print(e)
            db.rollback()

    return m
