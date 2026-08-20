from fastapi import Depends, HTTPException, status
from app.services.auth import get_current_user
from app.modules.user.models import User
from app.utils.utils import UserRole


def require_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado."
        )

    return current_user


def require_manager(
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado."
        )

    return current_user


def require_employee(
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "manager", "employee"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado."
        )

    return current_user