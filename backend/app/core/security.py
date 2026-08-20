from datetime import datetime, timedelta, timezone
import bcrypt
from jose import jwt, JWTError

from fastapi import HTTPException, status

from app.core.config import settings



# =========================
# PASSWORD HASH
# =========================

def get_hash_password(password: str) -> str:
    # Converte a senha para bytes
    pwd_bytes = password.encode('utf-8')
    # Gera o salt e o hash
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # Retorna como string para salvar no banco
    return hashed_password.decode('utf-8')



def verify_password(
    plain_password: str, 
    hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_bytes)

# =========================
# JWT TOKEN
# =========================

def create_access_token(
    data: dict
):
    """
    Cria um token JWT para autenticação.
    """

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })


    token = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token



# =========================
# DECODIFICAR TOKEN
# =========================

def decode_access_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[
                settings.ALGORITHM
            ]
        )

        return payload


    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
