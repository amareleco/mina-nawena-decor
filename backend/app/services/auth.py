from typing import Optional, List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.utils.utils import UserRole
from app.core.security import verify_password, create_access_token
from app.modules.user.models import User
from app.services.auth_schemas import TokenPayload

# Define onde o Swagger/OpenAPI vai buscar o token JWT (URL da rota de login)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """
    Busca o usuário pelo e-mail e valida se a senha informada bate com o hash.
    """
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    Injeção de dependência para proteger rotas.
    Decodifica o token JWT, valida a expiração e retorna o objeto do usuário logado.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível autenticar as credenciais informadas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodifica o token JWT usando a SECRET_KEY
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenPayload(sub=user_id)
    except JWTError:
        raise credentials_exception

    # Busca o usuário no banco de dados pelo ID contido no token
    user = db.query(User).filter(User.id == int(token_data.sub)).first()
    if not user:
        raise credentials_exception
        
    # Bloqueia acesso caso o usuário tenha sido desativado no sistema
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuário inativo no sistema"
        )
        
    return user




# sua função que pega o usuário do token JWT
class RoleChecker:
    def __init__(self, allowed_roles: List[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        current_user: User = Depends(get_current_user)
    ) -> User:

        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Ação negada: você não possui as permissões necessárias."
            )

        return current_user

