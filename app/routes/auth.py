from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import (
    schemas,
    crud
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/register",
    response_model=schemas.UserResponse
)
def register(
    data: schemas.UserRegister,
    db: Session = Depends(get_db)
):

    return crud.register_user(
        db,
        data
    )


@router.post(
    "/login",
    response_model=schemas.TokenResponse
)
def login(
    data: schemas.UserLogin,
    db: Session = Depends(get_db)
):

    return crud.login_user(
        db,
        data
    )