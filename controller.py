#from db import SessionLocal, engine, Base
#from models import Filme
from schema import Task
from fastapi import FastAPI
from typing import List, Optional
from main import tasks,read_tasks

#app = FastAPI()

#Base.metadata.create_all(bind=engine)

a = tasks

def add_banco_de_dados(a):
    read_tasks()
    

add_banco_de_dados(a=a)