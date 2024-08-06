from sqlalchemy.orm import Session

from models.player import Player
from dto.player import PlayerDTO


# Получить список всех мужчин
def get_all_men(db: Session):
    return db.query(Player).filter_by(sex=1).all()


# Получить список всех женщин
def get_all_women(db: Session):
    return db.query(Player).filter_by(sex=2).all()


def get_player_by_id(db: Session, player_id: int):
    ...


# Внести изменения в игрока по id
def update_player_by_id(db: Session, player_id: int, data: PlayerDTO):
    player = db.query(Player).filter_by(id=player_id).first()
    player.name = data.name
    player.surname = data.surname
    player.patronymic = data.patronymic
    player.sex = data.sex
    player.department = data.department
    player.rating = data.rating

    try:
        db.add(player)
        db.commit()
        db.refresh(player)
    except Exception as e:
        db.rollback()
        print(e)

    return player


# Удалить игрока по id
def delete_player_by_id(db: Session, player_id: int):
    player = db.query(Player).filter_by(id=player_id).delete()
    db.commit()
    db.refresh(player)
    return player


# Добавить игрока
def create_new_player(db: Session, data: PlayerDTO):
    new_player = Player(
        surname=data.surname,
        name=data.name,
        patronymic=data.patronymic,
        sex=data.sex,
        department_id=data.department_id,
        rating=data.rating)

    try:
        db.add(new_player)
        db.commit()
        db.refresh(new_player)
    except Exception as e:
        db.rollback()
        print(e)

    return new_player
