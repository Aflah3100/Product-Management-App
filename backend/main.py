from fastapi import FastAPI
import database_models
from database_config import db_engine

server =FastAPI()


@server.on_event("startup")
def on_startup():
    #Creating database
    database_models.Base.metadata.create_all(bind=db_engine)


@server.get("/")
def fetchWelcome():
    return {
        "message":"Welcome to the API Server"
    }