# Exemplo de uso em qualquer rota no futuro:
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal, engine, get_db

router = APIRouter()

@router.get("/exemplo")
def exemplo_route(db: Session = Depends(get_db)):
    # Sua lógica usando a sessão do banco aqui...
    pass