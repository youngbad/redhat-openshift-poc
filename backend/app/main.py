from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import Base, engine, get_db

# Create all tables on startup (fine for a simple demo app; use Alembic migrations in production).
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/items", response_model=list[schemas.ItemRead])
def list_items(db: Session = Depends(get_db)):
    return db.query(models.Item).order_by(models.Item.id).all()


@app.post("/api/items", response_model=schemas.ItemRead, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(title=item.title, completed=item.completed)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
