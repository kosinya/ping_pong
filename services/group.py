from sqlalchemy import text
from starlette.responses import JSONResponse

from models.group import Group
from models.player import Player
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
    query = text("""SELECT g.*, p.surname, p.name, p.patronymic
                    FROM groups g
                    JOIN players p ON g.player_id = p.player_id
                    ORDER BY g.group_name ASC;""")
    results = db.execute(query).fetchall()
    data = []
    if results:
        for r in results:
            data.append({
                "id": r[0],
                "player_id": r[1],
                "score": r[2],
                "group_name": r[3],
                "league_id": r[4],
                "surname": r[5],
                "name": r[6],
                "patronymic": r[7]
            })
    return JSONResponse(content=data, status_code=200)
