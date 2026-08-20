from datetime import date

from sqlalchemy import String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Supplier(Base):

    __tablename__ = "suppliers"


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


    contact: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )


    email: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    address: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    created_at: Mapped[date] = mapped_column(
        Date,
        default=date.today
    )