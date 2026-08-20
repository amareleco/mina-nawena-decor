from sqlalchemy.orm import Session

from app.modules.product.models import Product
from app.modules.product.schemas import (
    ProductCreate,
    ProductUpdate
)

from app.modules.category.models import Category



def generate_product_code(
    db: Session
) -> str:

    last_product = (
        db.query(Product)
        .order_by(Product.id.desc())
        .first()
    )

    if not last_product:
        number = 1
    else:
        number = last_product.id + 1

    return f"PROD-{number:03d}"



def create_product(
    db: Session,
    product: ProductCreate
):

    category = (
        db.query(Category)
        .filter(
            Category.id == product.category_id
        )
        .first()
    )

    if not category:
        return None

    new_product = Product(
        code=generate_product_code(db),
        name=product.name,
        description=product.description,
        category_id=product.category_id,
        quantity=product.quantity,
        minimum_stock=product.minimum_stock,
        is_active=product.is_active
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product



def get_products(
    db: Session
):

    return (
        db.query(Product)
        .all()
    )



def get_product_by_code(
    db: Session,
    code: str
):

    return (
        db.query(Product)
        .filter(
            Product.code == code
        )
        .first()
    )


def update_product(
    db: Session,
    code: str,
    product_data: ProductUpdate
):

    product = get_product_by_code(
        db,
        code
    )

    if not product:
        return None


    if product_data.quantity < 0:
        return None


    product.quantity = product_data.quantity


    db.commit()

    db.refresh(product)

    return product



def delete_product(
    db: Session,
    code: str
):

    product = get_product_by_code(
        db,
        code
    )


    if not product:
        return None


    db.delete(product)

    db.commit()


    return product