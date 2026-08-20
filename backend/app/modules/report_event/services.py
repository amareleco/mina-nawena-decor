from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.modules.event.models import Event
from app.modules.event_item.models import EventItem

from app.modules.report_event.schemas import (
    ReportHeader,
    EventReportItem,
    EventItemReport,
    EventReportResponse,
)


def get_events_report(
    db: Session
):

    events = (
        db.query(Event)
        .options(
            joinedload(Event.client),
            joinedload(Event.items)
            .joinedload(EventItem.product)
        )
        .order_by(
            Event.event_date.desc()
        )
        .all()
    )


    report_items = []


    for event in events:

        items = []

        for item in event.items:

            items.append(
                EventItemReport(
                    product_code=item.product.code,
                    product_name=item.product.name,
                    quantity=item.quantity
                )
            )


        report_items.append(
            EventReportItem(
                event_code=event.code,
                event_name=event.name,

                client_code=event.client.code,
                client_name=event.client.name,

                event_date=event.event_date,

                location=event.location,

                status=event.status,

                items=items
            )
        )


    header = ReportHeader(
        company="Mina Nawena hi Decor",
        report_name="Relatório de Eventos",
        generated_at=datetime.now(),
        total_records=len(report_items)
    )


    return EventReportResponse(
        header=header,
        data=report_items
    )