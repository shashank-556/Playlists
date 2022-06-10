from typing import List
from pydantic import BaseModel, Field

from models import Playlist,Item


class playlistInput(BaseModel):
    title: str = Field(...,max_length=30)
    is_public: bool = Field(True)


class playlistsOutput(playlistInput) :
    owner_id: int
    # items = List[Item] 

    class Config :
        orm_mode = True

class userBaseModel(BaseModel) :
    email:str = Field(...,max_length=40)
    name: str = Field(...,max_length=30)

class userOutputModel(userBaseModel) :
    id:int
    # playlists = List[Playlist]
    class Config:
        orm_mode = True

class userInputModel(userBaseModel) :
    password:str = Field(...,min_length=8)

class Token(BaseModel):
    access_token: str
    token_type: str


