from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routes import router

app = FastAPI()
SQLModel.metadata.create_all(engine)
app.include_router(router, prefix='/api')
