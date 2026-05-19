from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal

from app.email_utils import send_welcome_email

from app.dependencies import get_db

from app.auth import pwd_context

from app import (
    schemas,
    crud,
    models
)

from app.auth import (
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)




@router.post("/register")
async def register(
    user: schemas.UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = models.User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password,
        phone=user.phone,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    await send_welcome_email(
        user.email,
        user.full_name
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.user_id
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role.value
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }