from sqlalchemy.orm import Session
import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


async def create_user(db:Session,usr:schemas.userInputModel) :
    db_user = models.User(**usr.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_playlists(db: Session,user: models.User ):
    return db.query(models.Playlist).filter(models.Playlist.owner_id == user.id).all()


def create_playlists(db: Session, play: schemas.playlistInput, user_id: int):
    play = models.Playlist(**play.dict(), owner_id=user_id)
    db.add(play)
    db.commit()
    db.refresh(play)
    return play
