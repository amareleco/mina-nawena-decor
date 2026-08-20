from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.session import get_db

from app.modules.login.schemas import (
    LoginRequest,
    TokenResponse
)

from app.services.auth import authenticate_user

from app.core.security import create_access_token # Importe a função que gera o token JWT


router = APIRouter(
    prefix="/login",
    tags=["Login"]
)


@router.post("/access-token", response_model= TokenResponse)
def login_access_token(
    data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    """
    Endpoint para autenticação de usuários.
    Recebe email e senha, valida as credenciais e retorna um token JWT.
    """
    user = authenticate_user(db, email = data.username, password = data.password)
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha incorretos"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário inativo no sistema"
        )
    
    # Gera o token JWT usando a função create_access_token
    token = create_access_token(data={"sub": str(user.id)})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }       


