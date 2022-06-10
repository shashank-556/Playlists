from database import SessionLocal
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,Depends
import ujson
from crud import get_user_by_email, get_user_by_id

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

with open('secrets.json','r') as fh :
    js = ujson.load(fh)
    SECRET_KEY = js["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 10

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_pass,hash_pass) :
    return pwd_context.verify(plain_pass,hash_pass)

def get_password_hash(plain_pass) :
    return pwd_context.hash(plain_pass)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme),db = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        userid = payload.get("sub")
        if userid is None:
            raise credentials_exception
    except JWTError as e:
        # print(e)
        raise credentials_exception
    
    user = get_user_by_id(db,user_id=int(userid))
    if user is None:
        raise credentials_exception
    return user

def authenticate_user(db, useremail: int, password: str):
    user = get_user_by_email(db,useremail)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
