from fastapi import APIRouter

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/")
def get_all_jobs():

    return {
        "message": "All Jobs Fetched Successfully"
    }


@router.get("/{job_id}")
def get_job_by_id(job_id: int):

    return {
        "message": f"Job {job_id} fetched successfully"
    }