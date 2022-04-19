from .database import Base
from sqlalchemy import Column, Integer, String

class DbCompany(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    companyname = Column(String)
    companyname_furigana = Column(String)
    zipcode = Column(String)
    address = Column(String)
    company_cp = Column(String)
    company_description = Column(String)
    image_url = Column(String)