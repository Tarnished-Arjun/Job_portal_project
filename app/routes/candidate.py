from fastapi import APIRouter

router = APIRouter(
    prefix="/candidate",
    tags=["Candidate"]
)


@router.get("/")
def candidate_home():

    return {
        "message": "Candidate Route Working"
    }