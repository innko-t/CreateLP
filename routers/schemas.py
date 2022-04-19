from pydantic import BaseModel

class InfoBase(BaseModel):
    companyname: str
    companyname_furigana: str
    zipcode: str
    address: str
    company_cp: str
    company_description: str
    class Config():
        orm_mode=True
