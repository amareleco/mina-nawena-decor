from sqlalchemy import (
    ForeignKey,
    Integer,
    String
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class EventItem(Base):

    __tablename__ = "event_items"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    code: Mapped[str] = mapped_column(
    String(20),
    unique=True,
    index=True,
    nullable=False
    )


    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
        nullable=False
    )


    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )


    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )


    event: Mapped["Event"] = relationship(
        "Event",
        back_populates="items"
    )


    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="event_items"
    )