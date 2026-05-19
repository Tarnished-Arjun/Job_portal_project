from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.dependencies import get_db

from app import (
    models,
    schemas
)


router = APIRouter(
    prefix="/candidate",
    tags=["Candidate"]
)




@router.post("/")
def create_candidate_profile(
    data: schemas.CandidateCreate,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.user_id == data.user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    candidate = models.Candidate(
        user_id=data.user_id,
        no_of_experience=data.no_of_experience,
        skills=data.skills,
        linkedin_url=data.linkedin_url,
        github_url=data.github_url
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    return candidate


@router.get("/{candidate_id}")
def get_candidate_profile(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(
        models.Candidate
    ).filter(
        models.Candidate.id == candidate_id
    ).first()

    if not candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return candidate

@router.put("/{candidate_id}")
def update_candidate_profile(
    candidate_id: int,
    data: schemas.CandidateCreate,
    db: Session = Depends(get_db)
):

    candidate = db.query(
        models.Candidate
    ).filter(
        models.Candidate.id == candidate_id
    ).first()

    if not candidate:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    candidate.no_of_experience = data.no_of_experience
    candidate.skills = data.skills
    candidate.linkedin_url = data.linkedin_url
    candidate.github_url = data.github_url

    db.commit()

    db.refresh(candidate)

    return candidate