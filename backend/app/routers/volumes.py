from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Volume

router = APIRouter(prefix="/volumes", tags=["volumes"])

@router.get("")
def list_volumes(db: Session = Depends(get_db)):
    rows = db.query(Volume).order_by(Volume.volume_id.asc()).all()
    return [
        {
            "volume_id": row.volume_id,
            "title": row.title,
            "content_hash": row.content_hash,
        }
        for row in rows
    ]

@router.get("/{volume_id}")
def get_volume(volume_id: int, db: Session = Depends(get_db)):
    row = db.query(Volume).filter(Volume.volume_id == volume_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Volume not found")
    return row
