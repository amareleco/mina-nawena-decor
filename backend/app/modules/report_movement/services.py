from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.modules.movement.models import StockMovement

from app.modules.report_movement.schemas import (
    ReportHeader,
    MovementReportItem,
    MovementReportResponse,
)


def get_movements_report(
    db: Session
) -> MovementReportResponse:

    movements = (
        db.query(StockMovement)
        .options(
            joinedload(StockMovement.product)
        )
        .order_by(
            StockMovement.created_at.desc()
        )
        .all()
    )


    report_items = []


    for movement in movements:

        report_items.append(
            MovementReportItem(
                code=movement.code,

                product_code=movement.product.code,
                product_name=movement.product.name,

                movement_type=movement.movement_type,

                quantity=movement.quantity,

                reason=movement.reason,

                created_at=movement.created_at,
            )
        )


    header = ReportHeader(
        company="Mina Nawena Decor",
        report_name="Relatório de Movimentações",
        generated_at=datetime.now(),
        total_records=len(report_items),
    )


    return MovementReportResponse(
        header=header,
        data=report_items
    )