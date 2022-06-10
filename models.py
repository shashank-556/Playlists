from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40),unique = True,index = True)
    name = Column(String(30))
    password = Column(String)

    playlists = relationship("Playlist", back_populates="owner")

    def __repr__(self) -> str:
        return f"User(id = {self.id}, email = {self.email}, name = {self.name}"


class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_public = Column(Boolean,default = True)
    owner = relationship("User", back_populates="playlists")
    items = relationship("Item",cascade = "all, delete")

class Item(Base) :
    __tablename__ = 'items'
    id = Column(Integer,primary_key = True)
    playlist_id = Column(Integer,ForeignKey('playlist.id'))
    movie_id = Column(String(30))

    __table_args__ = (UniqueConstraint('playlist_id','movie_id',name = 'playlist_movie_uc'),)
