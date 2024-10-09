from database import Session
from models.playoff import Playoff
from models.match import Match
from dto import playoff


def create_playoff(db: Session, data: playoff.PlayoffCreate):
    new_playoff = Playoff(
        name=data.name,
        start_stage=data.start_stage,
        current_stage=data.current_stage,
        league_id=data.league_id
    )

    try:
        db.add(new_playoff)
        db.commit()
        db.refresh(new_playoff)
    except Exception as e:
        print(e)
        db.rollback()

    return new_playoff


def get_all_playoffs(db: Session, league_id: int):
    return db.query(Playoff).filter_by(league_id=league_id).all()


def get_the_grid(db, playoff_id: int, stage):
    matches = db.query(Match).filter_by(playoff_id=playoff_id).all()
    return build_tree(matches)


def build_tree(matches):
    tree = {}

    final_match = max(matches, key=lambda x: x.type)
    if final_match:
        tree = build_match_tree(final_match, matches, set())
    return tree


def build_match_tree(match, matches, processed_matches):
    match_dict = {
        "player1_id": match.player1_id,
        "player2_id": match.player2_id,
        "score": match.score,
        "winner_id": match.winner_id,
        "match_id": match.match_id,
        "type": match.type,
        "children": []
    }

    types = ['Финал', '1/2', '1/4', '1/8']
    current_stage_index = types.index(match_dict["type"])
    dependent_matches = []

    if current_stage_index < len(types):
        processed_matches.add(match.match_id)
        if match_dict["player1_id"] != -1:
            dependent_matches = [m for m in matches
                                 if types.index(m.type) == current_stage_index+1 and m.match_id not in processed_matches
                                 and (m.winner_id == match_dict["player1_id"] or m.winner_id == match_dict["player2_id"])]
        else:
            dependent_matches = [m for m in matches
                                 if types.index(m.type) == current_stage_index + 1
                                 and m.match_id not in processed_matches]
    for dependent_match in dependent_matches[:2]:
        match_dict["children"].append(build_match_tree(dependent_match, matches, processed_matches))

    return match_dict
