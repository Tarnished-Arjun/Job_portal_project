from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import models


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db)
):

    users = db.query(models.User).all()

    return users


@router.get("/jobs")
def get_all_jobs(
    db: Session = Depends(get_db)
):

    jobs = db.query(models.Job).all()

    return jobs