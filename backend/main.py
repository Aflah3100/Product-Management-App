from fastapi import FastAPI

server =FastAPI()


@server.get("/")
def fetchWelcome():
    return {
        "message":"Welcome to the API Server"
    }