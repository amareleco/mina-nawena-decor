from sqlalchemy.orm import Session

from app.modules.supplier.models import Supplier
from app.modules.supplier.schemas import (
    SupplierCreate,
    SupplierUpdate
)


def generate_supplier_code(
    db: Session
) -> str:

    last_supplier = (
        db.query(Supplier)
        .order_by(Supplier.id.desc())
        .first()
    )


    if not last_supplier:
        number = 1
    else:
        number = last_supplier.id + 1


    return f"SUP-{number:03d}"



def create_supplier(
    db: Session,
    supplier: SupplierCreate
):

    new_supplier = Supplier(

        code=generate_supplier_code(db),

        name=supplier.name,

        contact=supplier.contact,

        email=supplier.email,

        address=supplier.address
    )


    db.add(new_supplier)

    db.commit()

    db.refresh(new_supplier)


    return new_supplier



def get_suppliers(
    db: Session
):

    return (
        db.query(Supplier)
        .all()
    )



def get_supplier_by_code(
    db: Session,
    code: str
):

    return (
        db.query(Supplier)
        .filter(
            Supplier.code == code
        )
        .first()
    )



def update_supplier(
    db: Session,
    code: str,
    supplier_data: SupplierUpdate
):

    supplier = get_supplier_by_code(
        db,
        code
    )


    if not supplier:
        return None


    data = supplier_data.model_dump(
        exclude_unset=True
    )


    for key, value in data.items():

        setattr(
            supplier,
            key,
            value
        )


    db.commit()

    db.refresh(supplier)


    return supplier



def delete_supplier(
    db: Session,
    code: str
):

    supplier = get_supplier_by_code(
        db,
        code
    )


    if not supplier:
        return None


    db.delete(supplier)

    db.commit()


    return supplier