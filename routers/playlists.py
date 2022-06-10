import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db,get_current_user
from schemas import playlistsOutput, playlistInput
from crud import create_playlists,get_playlists

router = APIRouter(prefix="/playlist",tags=['Playlist'])

@router.post('/',status_code=201,response_model=playlistsOutput)
async def create_playlist(play:playlistInput,db: Session = Depends(get_db),user = Depends(get_current_user)) :
    return create_playlists(db,play,user.id)

@router.get('/',response_model=playlistsOutput)
async def see_all_playlist(Session = Depends(get_db),user = Depends(get_current_user)) :
    pass

