from pydantic import BaseModel

#Pydantic Product Model Class
class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: float

    class Config:
        orm_mode = True
