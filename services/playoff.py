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
    return build_bracket(matches, stage)


def build_bracket(matches, stage="Финал"):
    if not matches:
        return None

    stage_matches = [match for match in matches if match.type == stage]

    # Create a dictionary to store the bracket tree
    bracket = {}

    # Iterate over the stage matches
    for match in stage_matches:
        id = match.match_id,
        player1_id = match.player1_id,
        player2_id = match.player2_id,
        score = match.score

        # Create a new match node
        match_node = {
            'id': id,
            'player1_id': player1_id,
            'player2_id': player2_id,
            'score': score
        }

        # Recursively build the children nodes
        if stage != 'Финал':
            next_stage = get_next_stage(stage)
            child_matches = [m for m in matches if
                             m.type == next_stage and (m.winner_id == match_node["player1_id"] or
                                                       m.winner_id == match_node["player2_id"])]
            if child_matches:
                match_node['children'] = [build_bracket([child_match], next_stage, key) for child_match in
                                          child_matches]

        bracket[key] = match_node

    return bracket


def get_next_stage(stage):
    stages = ['Финал', '1/2', '1/4', '1/8']
    return stages[stages.index(stage) - 1]
