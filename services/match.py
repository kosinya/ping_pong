from fastapi.exceptions import HTTPException

from database import Session
from models.match import Match
from models.group import Group
from dto import match


def create_match(db: Session, data: match.MatchCreate):
    match = Match(
        player1_id=data.player1_id,
        player2_id=data.player2_id,
        type=data.type,
        group_name=data.group_name,
        stage=data.stage,
        league_id=data.league_id
    )

    try:
        db.add(match)
        db.commit()
        db.refresh(match)
    except Exception as e:
        print(e)
        db.rollback()

    return match


def get_group_matches(db: Session, league_id: int):
    return db.query(Match).filter(id=league_id, type="Групповой").all()


def get_matches_by_stage(db: Session, league_id: int, stage: str):
    return db.query(Match).filter(id=league_id, stage=stage).all()


def update_match_result(db: Session, id: int, winner_id: int):
    m = db.query(Match).filter_by(id=id).first()
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
