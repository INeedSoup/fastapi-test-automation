# apiserver.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Calculation

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Dependency to provide a database session
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
    record = Calculation(operation="add", num1=num1, num2=num2, result=result)
    db.add(record)
    db.commit()
    return {"result": result}

@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int, db: Session = Depends(get_db)):
    result = num1 - num2
    record = Calculation(operation="subtract", num1=num1, num2=num2, result=result)
    db.add(record)
    db.commit()
    return {"result": result}

@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int, db: Session = Depends(get_db)):
    result = num1 * num2
    record = Calculation(operation="multiply", num1=num1, num2=num2, result=result)
    db.add(record)
    db.commit()
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apiserver:app", host="0.0.0.0", port=8000, reload=True)

