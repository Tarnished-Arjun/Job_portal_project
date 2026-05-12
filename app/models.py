from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum
)

from sqlalchemy.orm import relationship

from app.database import Base

import enum


class UserRole(enum.Enum):

    candidate = "candidate"

    employer = "employer"

    admin = "admin"


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100)
    )

    email = Column(
        String(100),
        unique=True
    )

    hashed_password = Column(
        String(255)
    )

    phone = Column(
        String(20)
    )

    role = Column(
        Enum(UserRole)
    )

    candidate_profile = relationship(
        "Candidate",
        back_populates="user",
        uselist=False
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

    no_of_experience = Column(
        Integer
    )

    skills = Column(
        String(255)
    )

    linkedin_url = Column(
        String(255)
    )

    github_url = Column(
        String(255)
    )

    user = relationship(
        "User",
        back_populates="candidate_profile"
    )