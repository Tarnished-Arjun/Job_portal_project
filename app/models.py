from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum,
    Text,
    Table
)

from sqlalchemy.orm import relationship

from app.database import Base

import enum

class UserRole(enum.Enum):

    candidate = "candidate"

    employer = "employer"

    admin = "admin"


saved_jobs = Table(
    "saved_jobs",
    Base.metadata,

    Column(
        "user_id",
        Integer,
        ForeignKey("users.user_id")
    ),

    Column(
        "job_id",
        Integer,
        ForeignKey("jobs.id")
    )
)


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(String(100))

    email = Column(
        String(100),
        unique=True
    )

    hashed_password = Column(String(255))

    phone = Column(String(20))

    role = Column(Enum(UserRole))

    candidate_profile = relationship(
        "Candidate",
        back_populates="user",
        uselist=False
    )

    employer_profile = relationship(
        "Employer",
        back_populates="user",
        uselist=False
    )

    saved_jobs_relation = relationship(
        "Job",
        secondary=saved_jobs,
        back_populates="saved_by_users"
    )


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    no_of_experience = Column(Integer)

    skills = Column(String(255))

    linkedin_url = Column(String(255))

    github_url = Column(String(255))

    user = relationship(
        "User",
        back_populates="candidate_profile"
    )


class Employer(Base):

    __tablename__ = "employers"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    company_name = Column(String(100))

    company_description = Column(Text)

    location = Column(String(100))

    website = Column(String(255))

    user = relationship(
        "User",
        back_populates="employer_profile"
    )

    jobs = relationship(
        "Job",
        back_populates="employer"
    )

class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(String(100))

    description = Column(Text)

    salary = Column(String(100))

    location = Column(String(100))

    experience_required = Column(Integer)

    employer_id = Column(
        Integer,
        ForeignKey("employers.id")
    )

    employer = relationship(
        "Employer",
        back_populates="jobs"
    )

    saved_by_users = relationship(
        "User",
        secondary=saved_jobs,
        back_populates="saved_jobs_relation"
    )

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    status = Column(String(50), default="Applied")