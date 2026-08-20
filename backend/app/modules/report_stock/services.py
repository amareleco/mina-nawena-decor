from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.modules.product.models import Product

from app.modules.report_stock.schemas import (
    ReportHeader,
    StockReportItem,
    StockReportResponse,
)


def get_stock_report(
    db: Session
):

    products = (
        db.query(Product)
        .options(
            joinedload(Product.category)
        )
        .order_by(Product.name)
        .all()
    )


    items = []


    for product in products:

        if product.quantity <= 0:
            status = "SEM ESTOQUE"

        elif product.quantity <= product.minimum_stock:
            status = "ESTOQUE BAIXO"

        else:
            status = "DISPONÍVEL"


        items.append(
            StockReportItem(

                product_code=product.code,

                product_name=product.name,

                category_name=(
                    product.category.name
                    if product.category
                    else None
                ),

                quantity=product.quantity,

                minimum_stock=product.minimum_stock,

                status=status
            )
        )


    header = ReportHeader(
        company="Mina Nawena hi decor",
        report_name="Relatório de Estoque Atual",
        generated_at=datetime.now(),
        total_records=len(items)
    )


    return StockReportResponse(
        header=header,
        data=items
    )