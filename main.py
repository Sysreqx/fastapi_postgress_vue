from fastapi import FastAPI
from engine import *
import model

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def start():
    return "Welcome to GosuDesk"