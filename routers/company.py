from routers.schemas import InfoBase
from db.database import get_db
from db import db_company
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import string
import random


router = APIRouter(
    prefix='/company',
    tags=['company']
)

@router.post('', response_model=InfoBase)
def create(request: InfoBase, db: Session = Depends(get_db)):
    return db_company.create(db, request)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(8))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
        return {
            'filename': path
        }



