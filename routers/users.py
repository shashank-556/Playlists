import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from fastapi import APIRouter, Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies import get_db,get_password_hash,authenticate_user,create_access_token,get_current_user
from schemas import userInputModel,userOutputModel,Token
from crud import create_user,get_user_by_email

router = APIRouter(prefix="/user",tags=['Users'])

@router.post('/',status_code=201,response_model=userOutputModel)
async def create_user_profile(usr:userInputModel,db:Session = Depends(get_db)) :
    if get_user_by_email(db,email=usr.email) :
        raise HTTPException(status_code=403,detail="An account with given email already exists")
    
    usr.password = get_password_hash(usr.password)
    return await create_user(usr=usr,db=db)


@router.get('/',response_model=userOutputModel)
async def user_profile(user = Depends(get_current_user)) :
    return user


@router.post('/login',response_model=Token,status_code=201)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": str(user.id),"name":user.name}
    )
    return {"access_token": access_token, "token_type": "bearer"}