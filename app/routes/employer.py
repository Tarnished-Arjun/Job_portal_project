from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(
    prefix="/employer",
    tags=["Employer"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


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