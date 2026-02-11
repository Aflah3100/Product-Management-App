from pydantic import BaseModel

class ProductModel(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:float

    class Config:
        orm_mode=True


