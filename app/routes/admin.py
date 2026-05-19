from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import models

from app.auth import admin_only

from app.dependencies import get_db


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)




@router.get("/jobs")
def get_all_jobs(
    current_user = Depends(admin_only),
    db: Session = Depends(get_db)
):

    jobs = db.query(models.Job).all()

    return jobs


@router.get("/users")
def get_all_users(
    current_user = Depends(admin_only),
    db: Session = Depends(get_db)
):

    users = db.query(models.User).all()

    return users