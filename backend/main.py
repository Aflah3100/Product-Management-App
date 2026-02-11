from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
import database_models
from database_config import db_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database import get_db_session
from typing import List
import models

server = FastAPI()


@server.on_event("startup")
def on_startup():
    # Creating database
    database_models.Base.metadata.create_all(bind=db_engine)


@server.get("/")
def show_welcome_message():
    return {"message": "Welcome to the API Server"}


# GET - Fetch all products from db
@server.get("/products", response_model=List[models.ProductModel])
def get_products(db_session: Session = Depends(get_db_session)):
    try:
        products = db_session.query(database_models.Product).all()

        return products

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error fetching products",
        )


# GET - Fetch product by id
@server.get("/products/{id}", response_model=models.ProductModel)
def get_product_by_id(id: int, db_session: Session = Depends(get_db_session)):
    try:
        product = (
            db_session.query(database_models.Product)
            .filter(database_models.Product.id == id)
            .first()
        )

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )
        else:
            return product

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error fetching product",
        )


# POST - Add product to db
@server.post("/product", response_model=models.ProductModel)
def add_product(
    product: models.ProductModel, db_session: Session = Depends(get_db_session)
):

    try:
        db_product = database_models.Product(**product.model_dump())
        db_session.add(db_product)
        db_session.commit()

        return db_product

    except IntegrityError:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Product already exists"
        )

    except SQLAlchemyError:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error Adding Product",
        )


# PUT - Update Product by id
@server.put("/product/{id}")
def update_product_by_id(
    id: int, product: models.ProductModel, db_session: Session = Depends(get_db_session)
):
    pass
