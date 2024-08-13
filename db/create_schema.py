from sqlalchemy import Integer, String, Date, Column, BigInteger
from sqlalchemy.orm import declarative_base
from datetime import date

from .connection import engine


BaseModel = declarative_base()


class Picture(BaseModel):
    __tablename__ = 'pictures'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    picture_url = Column(String(50), nullable=False)
    published = Column(Date, default=date.today)
    user_id = Column(BigInteger, nullable=False)


BaseModel.metadata.create_all(engine)