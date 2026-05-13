from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import (
    models,
    schemas
)


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_job(
    data: schemas.JobCreate,
    db: Session = Depends(get_db)
):

    job = models.Job(
        title=data.title,
        description=data.description,
        salary=data.salary,
        location=data.location,
        experience_required=data.experience_required,
        employer_id=data.employer_id
    )

    db.add(job)

    db.commit()

    db.refresh(job)

    return job