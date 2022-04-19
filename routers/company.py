from routers.schemas import InfoBase
from db.database import get_db
from db import db_company
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/company',
    tags=['company']
)

@router.post('', response_model=InfoBase)
def create(request: InfoBase, db: Session = Depends(get_db)):
    return db_company.create(db, request)