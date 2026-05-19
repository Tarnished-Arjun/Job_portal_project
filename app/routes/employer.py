from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

from app.dependencies import get_db

router = APIRouter(
    prefix="/employer",
    tags=["Employer"]
)



@router.post("/")
def create_employer_profile(
    data: schemas.EmployerCreate,
    db: Session = Depends(get_db)
):

    employer = models.Employer(
        user_id=data.user_id,
        company_name=data.company_name,
        company_description=data.company_description,
        location=data.location,
        website=data.website
    )

    db.add(employer)

    db.commit()

    db.refresh(employer)

    return employer


@router.get("/{employer_id}")
def get_employer_profile(
    employer_id: int,
    db: Session = Depends(get_db)
):

    employer = db.query(models.Employer).filter(
        models.Employer.id == employer_id
    ).first()

    if not employer:

        raise HTTPException(
            status_code=404,
            detail="Employer not found"
        )

    return employer

@router.get("/{employer_id}/applications")
def get_applications_for_employer(
    employer_id: int,
    db: Session = Depends(get_db)
):

    employer = db.query(models.Employer).filter(
        models.Employer.id == employer_id
    ).first()

    if not employer:
        raise HTTPException(
            status_code=404,
            detail="Employer not found"
        )

    jobs = db.query(models.Job).filter(
        models.Job.employer_id == employer_id
    ).all()

    result = []

    for job in jobs:

        applications = db.query(
            models.JobApplication
        ).filter(
            models.JobApplication.job_id == job.id
        ).all()

        for application in applications:

            candidate = db.query(models.Candidate).filter(
                models.Candidate.id == application.candidate_id
            ).first()

            result.append({
                "job_title": job.title,
                "candidate_id": candidate.id,
                "skills": candidate.skills,
                "experience": candidate.no_of_experience
            })

    return result