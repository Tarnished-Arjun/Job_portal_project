from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas

from app.dependencies import get_db

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post("/")
def apply_for_job(
    data: schemas.JobApplicationCreate,
    db: Session = Depends(get_db)
):

    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == data.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    job = db.query(models.Job).filter(
        models.Job.id == data.job_id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    application = models.JobApplication(
        candidate_id=data.candidate_id,
        job_id=data.job_id
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return {
        "message": "Applied successfully",
        "application_id": application.id
    }