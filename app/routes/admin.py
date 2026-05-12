from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users")
def get_all_users():

    return {
        "message": "Get All Users"
    }