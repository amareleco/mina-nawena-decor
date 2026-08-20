from sqlalchemy import String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from datetime import date
from app.utils.utils import UserRole

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, native_enum=True, values_callable=lambda x: [e.value for e in x]),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    created_at: Mapped[date] = mapped_column(
        Date,
        default=date.today
    )