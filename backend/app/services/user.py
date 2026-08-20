from sqlalchemy.orm import Session

from app.modules.user.models import User
from app.modules.user.schemas import UserCreate, UserUpdate

from app.core.security import get_hash_password


def generate_user_code(db: Session) -> str:
    last_user = (
        db.query(User)
        .order_by(User.id.desc())
        .first()
    )

    if not last_user:
        number = 1
    else:
        number = last_user.id + 1

    return f"DECOR-{number:03d}"


def create_user(
    db: Session,
    user: UserCreate
):

    print("ROLE RECEBIDO:", user.role)
    print("ROLE VALUE:", user.role.value)



    new_user = User(
        code=generate_user_code(db),
        name=user.name,
        email=user.email,
        password=get_hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def get_users(
    db: Session
):

    return (
        db.query(User)
        .all()
    )



def get_user_by_code(
    db: Session,
    code: str
):

    return (
        db.query(User)
        .filter(User.code == code)
        .first()
    )



def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )



def update_user(
    db: Session,
    code: str,
    user_data: UserUpdate
):

    user = get_user_by_code(
        db,
        code
    )

    if not user:
        return None


    data = user_data.model_dump(
        exclude_unset=True
    )


    for key, value in data.items():

        setattr(
            user,
            key,
            value
        )

    if user_data.password:
        user.password = get_hash_password (user_data.password)


    db.commit()
    db.refresh(user)

    return user



def delete_user(
    db: Session,
    code: str
):

    user = get_user_by_code(
        db,
        code
    )

    if not user:
        return None


    db.delete(user)

    db.commit()

    return user