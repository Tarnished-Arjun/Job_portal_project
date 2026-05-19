from fastapi import APIRouter, Depends, HTTPException


from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import models

from app.dependencies import get_db


router = APIRouter(
    prefix="/saved-jobs",
    tags=["Saved Jobs"]
)




@router.post("/{user_id}/{job_id}")
def save_job(
    user_id: int,
    job_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.user_id == user_id
    ).first()

    job = db.query(models.Job).filter(
        models.Job.id == job_id
    ).first()

    if not user or not job:

        raise HTTPException(
            status_code=404,
            detail="User or Job not found"
        )

    user.saved_jobs_relation.append(job)

    db.commit()

    return {
        "message": "Job saved successfully"
    }


@router.get("/{user_id}")
def get_saved_jobs(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.user_id == user_id
    ).first()

    return user.saved_jobs_relation