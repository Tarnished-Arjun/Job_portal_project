from fastapi import APIRouter

router = APIRouter(
    prefix="/saved-jobs",
    tags=["Saved Jobs"]
)


@router.get("/")
def saved_jobs():

    return {
        "message": "Saved Jobs Route Working"
    }