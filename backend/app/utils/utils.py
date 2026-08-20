
# Code auxiliar para resolver problema de incompatibilidade entre schema e campos presentes no banco
# de dados

from datetime import datetime

from enum import Enum

def serialize_event_item(item):

    return {
        "code": item.code,
        "event_code": item.event.code,
        "product_code": item.product.code,
        "quantity": item.quantity
    }


# serializacao de campo de resposta de movimento
def stock_movement_response(item):

    return {
        "code": item.code,
        "product_code": item.product.code,
        "product_name": item.product.name,
        "movement_type": item.movement_type,
        "quantity": item.quantity,
        "reason": item.reason,
        "created_at":  item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": item.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    }

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"  
    EMPLOYEE = "employee"


