from datetime import date

from sqlalchemy import (
    String,
    Date,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Event(Base):

    __tablename__ = "events"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False
    )


    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False
    )


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )


    event_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )


    event_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )


    location: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    status: Mapped[str] = mapped_column(
        String(30),
        default="Planejado"
    )


    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )


    created_at: Mapped[date] = mapped_column(
        Date,
        default=date.today
    )


    client: Mapped["Client"] = relationship(
        "Client",
        back_populates="events"
    )

    items: Mapped[list["EventItem"]] = relationship(
    "EventItem",
    back_populates="event",
    cascade="all, delete-orphan"
)