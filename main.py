
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db, Base


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI
app = FastAPI(
    title="Business Records API",
    description="A REST API for managing business records",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Business Records API!",
        "status": "Running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Business Records API"
    }


# CREATE: Add a new business record
@app.post(
    "/records/",
    response_model=schemas.BusinessRecordResponse,
    status_code=status.HTTP_201_CREATED
)
def create_record(
    record: schemas.BusinessRecordCreate,
    db: Session = Depends(get_db)
):
    new_record = models.BusinessRecord(**record.model_dump())

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


# READ: Get all business records
@app.get(
    "/records/",
    response_model=List[schemas.BusinessRecordResponse]
)
def get_records(db: Session = Depends(get_db)):
    return db.query(models.BusinessRecord).all()


# READ: Get one business record by ID
@app.get(
    "/records/{record_id}",
    response_model=schemas.BusinessRecordResponse
)
def get_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(models.BusinessRecord).filter(
        models.BusinessRecord.id == record_id
    ).first()

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    return record


# UPDATE: Modify an existing business record
@app.put(
    "/records/{record_id}",
    response_model=schemas.BusinessRecordResponse
)
def update_record(
    record_id: int,
    updated_data: schemas.BusinessRecordUpdate,
    db: Session = Depends(get_db)
):
    record = db.query(models.BusinessRecord).filter(
        models.BusinessRecord.id == record_id
    ).first()

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    changes = updated_data.model_dump(exclude_unset=True)

    for key, value in changes.items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)

    return record


# DELETE: Remove a business record
@app.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(models.BusinessRecord).filter(
        models.BusinessRecord.id == record_id
    ).first()

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    db.delete(record)
    db.commit()

    return {
        "message": "Business record deleted successfully",
        "record_id": record_id
    }
