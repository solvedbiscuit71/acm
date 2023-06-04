import os
import dotenv

from bcrypt import hashpw, checkpw

dotenv.load_dotenv()
salt = os.getenv('SALT').encode()


def hash_password(passwd: str) -> str:
    return hashpw(passwd.encode(), salt).decode()


def validate_password(passwd: str, hashed_passwd: str) -> bool:
    return checkpw(passwd.encode(), hashed_passwd.encode())
