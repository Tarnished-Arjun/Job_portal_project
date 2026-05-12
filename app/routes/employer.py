from fastapi import APIRouter

router = APIRouter(
    prefix="/employer",
    tags=["Employer"]
)


@router.get("/")
def employer_home():

    return {
        "message": "Employer Route Working"
    }