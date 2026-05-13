from pydantic import BaseModel

from app.models import UserRole


class UserRegister(BaseModel):

    full_name: str

    email: str

    password: str

    phone: str

    role: UserRole


class UserLogin(BaseModel):

    email: str

    password: str


class TokenResponse(BaseModel):

    access_token: str

    token_type: str


class UserResponse(BaseModel):

    user_id: int

    full_name: str

    email: str

    phone: str

    role: UserRole

    class Config:
        from_attributes = True


class JobCreate(BaseModel):

    title: str

    description: str

    salary: str

    location: str

    experience_required: int

    employer_id: int


class CandidateCreate(BaseModel):

    user_id: int

    no_of_experience: int

    skills: str

    linkedin_url: str

    github_url: str


class EmployerCreate(BaseModel):

    user_id: int

    company_name: str

    company_description: str

    location: str

    website: str


class JobResponse(BaseModel):

    id: int

    title: str

    description: str

    salary: str

    location: str

    experience_required: int

    class Config:
        from_attributes = True