from sqlalchemy.orm import Session

from app.modules.category.models import Category
from app.modules.category.schemas import (
    CategoryCreate,
    CategoryUpdate
)


def generate_category_code(
    db: Session
) -> str:

    last_category = (
        db.query(Category)
        .order_by(Category.id.desc())
        .first()
    )

    if not last_category:
        number = 1
    else:
        number = last_category.id + 1

    return f"CAT-{number:03d}"



def create_category(
    db: Session,
    category: CategoryCreate
):

    new_category = Category(
        code=generate_category_code(db),
        name=category.name,
        description=category.description
    )

    db.add(new_category)

    db.commit()

    db.refresh(new_category)

    return new_category



def get_categories(
    db: Session
):

    return (
        db.query(Category)
        .all()
    )



def get_category_by_code(
    db: Session,
    code: str
):

    return (
        db.query(Category)
        .filter(Category.code == code)
        .first()
    )



def update_category(
    db: Session,
    code: str,
    category_data: CategoryUpdate
):

    category = get_category_by_code(
        db,
        code
    )

    if not category:
        return None


    data = category_data.model_dump(
        exclude_unset=True
    )


    for key, value in data.items():

        setattr(
            category,
            key,
            value
        )


    db.commit()

    db.refresh(category)

    return category



def delete_category(
    db: Session,
    code: str
):

    category = get_category_by_code(
        db,
        code
    )

    if not category:
        return None


    db.delete(category)

    db.commit()

    return category