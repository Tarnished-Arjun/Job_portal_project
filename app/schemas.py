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


class CandidateCreate(BaseModel):

    no_of_experience: int

    skills: str

    linkedin_url: str

    github_url: str

class CandidateResponse(BaseModel):

    id: int

    no_of_experience: int

    skills: str

    linkedin_url: str

    github_url: str

    class Config:
        from_attributes = True