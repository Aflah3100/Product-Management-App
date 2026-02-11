from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Column,Integer,String,Float

#Database Product Model
class Product(Base):

    __tablename__="Products"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)