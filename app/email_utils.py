from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

async def send_welcome_email(email: EmailStr, username: str):

    html = f"""
    <h2>Hello {username}</h2>

    <p>Welcome to Job Portal API</p>

    <p>Your account has been created successfully.</p>

    <br>

    <p>Regards,</p>
    <p>Arjun Krishna</p>
    """

    message = MessageSchema(
        subject="Welcome to Job Portal API",
        recipients=[email],
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)

    await fm.send_message(message)