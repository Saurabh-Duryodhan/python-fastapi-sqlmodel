from sqlmodel import create_engine, Session
from typing import Generator
from models import *


conn_str = 'mysql+pymysql://root:password@localhost:3306/relationaldb'


engine = create_engine(conn_str, echo=True)

def get_db() -> Generator:
    with Session(engine) as db:
        yield d