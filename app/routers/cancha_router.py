from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.routers.deps.db_sessions import SessionDep
from app.models.cancha import Cancha, MostrarCancha, CanchaBase

canchas_router = APIRouter (prefix="/canchas", tags=["Canchas"])

@canchas_router.get("/", response_model=List[MostrarCancha])
def obtener_canchas(db: SessionDep):
    canchas = db.exec(select(Cancha)).all()
    return canchas

@canchas_router.post("/", response_model=MostrarCancha)
def crear_cancha(cancha: CanchaBase, db: SessionDep):
    nueva_cancha = Cancha.from_orm(cancha)
    db.add(nueva_cancha)
    db.commit()
    db.refresh(nueva_cancha)
    return nueva_cancha

@canchas_router.get("/{id}", response_model=MostrarCancha)
def obtener_cancha(id: int, db: SessionDep):
    cancha = db.get(Cancha, id)
    if not cancha:
        raise HTTPException(status_code=404, detail="Cancha no encontrada")
    return cancha
