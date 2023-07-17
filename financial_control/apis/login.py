from sqlalchemy.orm import Session
from jose import jwt
from jose import JWTError

from fastapi import APIRouter, Depends, HTTPException, status, encoders
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from financial_control.core.config import settings
from financial_control.schemas.token import Token
from financial_control.schemas.user import UserOutput
from financial_control.core.security import create_access_token, verify_password
from financial_control.database.config import get_database
from financial_control.services.user import get_user


router = APIRouter()


@router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def login_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_database)):
    user = await authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
        )
    access_token = create_access_token(data={"sub": user.email})
    user_decode = UserOutput(**encoders.jsonable_encoder(user)).model_dump()
    return {"access_token": access_token, "token_type": "bearer", "user": user_decode}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_database)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(email=username, db=db)
    if user is None:
        raise credentials_exception
    return user

async def authenticate_user(email: str, password: str, db: Session):
    user = await get_user(email=email, db=db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user