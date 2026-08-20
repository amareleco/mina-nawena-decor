from sqlalchemy.orm import Session

from fastapi import HTTPException, status

from app.modules.movement.models import StockMovement
from app.modules.movement.schemas import (
    StockMovementCreate,
    StockMovementUpdate,
    MovementType
)

from app.modules.product.models import Product

from app.utils.utils import stock_movement_response

def generate_stock_movement_code(db: Session):

    last = (
        db.query(StockMovement)
        .order_by(StockMovement.id.desc())
        .first()
    )

    if not last:
        return "MOV-001"

    number = int(last.code.split("-")[1]) + 1

    return f"MOV-{number:03d}"

def create_stock_movement(
    db: Session,
    data: StockMovementCreate
):
    product = (
        db.query(Product)
        .filter(Product.id == data.product_id)
        .first()
    )

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    tipo_movimento = str(data.movement_type.value if hasattr(data.movement_type, 'value') else data.movement_type).upper()

    # ✅ ENTRADA e DEVOLUÇÃO: apenas adiciona
    if tipo_movimento in ["ENTRADA", "DEVOLUCAO"]:
        product.quantity += data.quantity

    # ✅ SAÍDA e DANIFICADO: verifica ANTES de remover
    elif tipo_movimento in ["SAIDA", "DANIFICADO"]:
        if product.quantity < data.quantity:
            raise HTTPException(
                status_code=400,
                detail="Quantidade insuficiente em estoque"
            )
        product.quantity -= data.quantity

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo de movimentação inválido: {data.movement_type}"
        )

    movement = StockMovement(
        code=generate_stock_movement_code(db),
        product_id=product.id,
        movement_type=data.movement_type.value,
        quantity=data.quantity,
        reason=data.reason
    )

    db.add(product)
    db.add(movement)
    db.commit()
    db.refresh(movement)

    return stock_movement_response(movement)


def get_stock_movement_by_code(
    db: Session,
    code: str
):

    movement = (
        db.query(StockMovement)
        .filter(
            StockMovement.code == code
        )
        .first()
    )


    if not movement:
        raise HTTPException(
            status_code=404,
            detail="Movimento não encontrado"
        )


    return stock_movement_response(movement)

def get_stock_movements(db: Session):

    movements = db.query(StockMovement).all()

    return [
        stock_movement_response(item)
        for item in movements
    ]


def update_stock_movement(
    db: Session,
    code: str,
    data: StockMovementUpdate,
):

    movement = (
        db.query(StockMovement)
        .filter(StockMovement.code == code)
        .first()
    )

    if not movement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimento não encontrado."
        )
    
      # Atualizar apenas os campos fornecidos (exclude_unset=True ignora campos não setados)
    data_to_update = data.model_dump(exclude_unset=True)

    # Remove created_at caso esteja tentando atualizar (segurança extra)
    data_to_update.pop("created_at", None)

    # Atualizar tudo de uma vez
    for key, value in data_to_update.items():
        setattr(movement, key, value)


    if data.quantity is not None:
        movement.quantity = data.quantity

    if data.reason is not None:
        movement.reason = data.reason

    db.commit()

    db.refresh(movement)

    return stock_movement_response(movement)


def delete_stock_movement(
    db: Session,
    code: str,
):

    movement = (
        db.query(StockMovement)
        .filter(StockMovement.code == code)
        .first()
    )

    if not movement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimento não encontrado."
        )

    db.delete(movement)

    db.commit()

    return {"detail": "Movimento removido com sucesso."}