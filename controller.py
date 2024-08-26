from db import SessionLocal, engine, Base
from models import Filme
from schema import Task
from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

