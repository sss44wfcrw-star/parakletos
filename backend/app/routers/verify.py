from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Volume
from ..services.verifier import verify_volume

router = APIRouter(prefix="/archive", tags=["verify"])

@router.get("/verify/{volume_id}")
def verify_archive(volume_id: int, db: Session = Depends(get_db)):
    row = db.query(Volume).filter(Volume.volume_id == volume_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Volume not found")

    result = verify_volume(volume_id=row.volume_id, content_length=len(row.content))
    return {
        "volume_id": row.volume_id,
        "title": row.title,
        "verification": result,
    }
