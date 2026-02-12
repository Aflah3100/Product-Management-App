from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
import database_models
from database_config import db_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database import get_db_session
from typing import List
import models

"""
API Documentation (Swagger):

Run the FastAPI application using:
    uvicorn main:server --reload

After the server starts, access the API documentation at:
- Swagger UI: http://localhost:8000/docs

"""

server = FastAPI()

server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)


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
@server.get("/product/{id}", response_model=models.ProductModel)
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
@server.put("/product/{id}", response_model=models.ProductModel)
def update_product_by_id(
    id: int, product: models.ProductModel, db_session: Session = Depends(get_db_session)
):
    try:
        db_product = (
            db_session.query(database_models.Product)
            .filter(database_models.Product.id == id)
            .first()
        )

        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )
        else:
            db_product.id = product.id
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db_product.quantity = product.quantity
            db_session.commit()
            db_session.refresh(db_product)

            return db_product

    except IntegrityError:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Product conflict error"
        )

    except SQLAlchemyError:
        db_session.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating product",
        )


# DELETE - Delete product from db
@server.delete("/product/{id}")
def delete_product(id: int, db_session: Session = Depends(get_db_session)):
    try:
        db_product = (
            db_session.query(database_models.Product)
            .filter(database_models.Product.id == id)
            .first()
        )

        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )
        else:
            db_session.delete(db_product)
            db_session.commit()
            return {"message": "Product deleted successfully"}

    except SQLAlchemyError:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting product",
        )
