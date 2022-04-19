from routers.schemas import InfoBase
from sqlalchemy.orm.session import Session
from db.models import DbCompany

def create(db:Session, request: InfoBase):
    new_company = DbCompany(
        companyname= request.companyname,
        companyname_furigana= request.companyname_furigana,
        zipcode= request.zipcode,
        address= request.address,
        company_cp= request.company_cp,
        company_description= request.company_description
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company