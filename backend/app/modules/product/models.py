from datetime import date

from sqlalchemy import String, Integer, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Product(Base):

    __tablename__ = "products"


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


    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )


    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    minimum_stock: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    created_at: Mapped[date] = mapped_column(
        Date,
        default=date.today
    )


    category: Mapped["Category"] = relationship(
    "Category",
    back_populates="products"
    )

    event_items: Mapped[list["EventItem"]] = relationship(
    "EventItem",
    back_populates="product"
    )

    stock_movements: Mapped[list["StockMovement"]] = relationship(
        "StockMovement",
        back_populates="product",
        cascade="all, delete-orphan"  #  DELETE TUDO quando produto for deletado
    )