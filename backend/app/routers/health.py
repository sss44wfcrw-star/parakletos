from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..db import get_db
from ..models import Volume

router = APIRouter()

@router.get("/health")
def health(db: Session = Depends(get_db)):
    volume_count = db.query(func.count(Volume.id)).scalar() or 0
    return {
        "status": "healthy",
        "backend": "online",
        "database": "connected",
        "volume_count": volume_count,
        "phi": 1.618033988749895,
        "resonance": 432.0,
    }
