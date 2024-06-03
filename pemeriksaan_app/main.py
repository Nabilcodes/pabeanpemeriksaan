from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, service
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/djbc/send_data_for_verification", response_model=schemas.Surat)
def send_data_for_verification(pib: schemas.PIBCreate, db: Session = Depends(get_db)):
    surat = service.verify_pib(db, pib)
    return surat

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
