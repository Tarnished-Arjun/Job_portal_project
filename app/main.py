from fastapi import FastAPI

from app.routes import (
    auth,
    jobs,
    admin,
    candidate,
    employer,
    saved_jobs
)

from app import models


app = FastAPI()


app.include_router(auth.router)

app.include_router(jobs.router)

app.include_router(admin.router)

app.include_router(candidate.router)

app.include_router(employer.router)

app.include_router(saved_jobs.router)


@app.get("/")
def home():

    return {
        "message": "Job Portal API Running"
    }