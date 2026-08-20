from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.modules.product.models import Product
from app.modules.report_product.schemas import (
    ReportHeader,
    ProductReportItem,
    ProductReportResponse,
)


def get_products_report(db: Session) -> ProductReportResponse:
    products = (
        db.query(Product)
        .options(
            joinedload(Product.category)
        )
        .order_by(Product.name)
        .all()
    )

    report_items = []

    for product in products:

        if product.quantity <= 0:
            stock_status = "OUT OF STOCK"
        elif product.quantity <= product.minimum_stock:
            stock_status = "LOW STOCK"
        else:
            stock_status = "IN STOCK"

        report_items.append(
            ProductReportItem(
                code=product.code,
                name=product.name,

                category_code=product.category.code if product.category else None,
                category_name=product.category.name if product.category else None,

                quantity=product.quantity,
                minimum_stock=product.minimum_stock,

                stock_status=stock_status
            )
        )

    header = ReportHeader(
        company="Mina Nawena Decor",
        report_name="Relatório de Produtos",
        generated_at=datetime.now(),
        total_records=len(report_items),
    )

    return ProductReportResponse(
        header=header,
        data=report_items,
    )