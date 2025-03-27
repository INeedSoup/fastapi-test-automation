from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Calculation

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI with PostgreSQL"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int, db: Session = Depends(get_db)):
    result = num1 + num2
    db_entry = Calculation(operation="add", num1=num1, num2=num2, result=result)
    db.add(db_entry)
    db.commit()
    return {"result": result}
