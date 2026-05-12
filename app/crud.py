from sqlalchemy.orm import Session

from fastapi import HTTPException

from app import (
    models,
    auth
)


def register_user(
    db: Session,
    data
):

    existing_user = db.query(
        models.User
    ).filter(
        models.User.email == data.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = auth.hash_password(
        data.password
    )

    user = models.User(
        full_name=data.full_name,
        email=data.email,
        hashed_password=hashed_password,
        phone=data.phone,
        role=data.role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(
    db: Session,
    data
):

    user = db.query(
        models.User
    ).filter(
        models.User.email == data.email
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not auth.verify_password(
        data.password,
        user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = auth.create_access_token(
        data={
            "sub": user.email,
            "role": user.role.value
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }