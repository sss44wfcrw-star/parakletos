from pydantic import BaseModel
from datetime import datetime

class VolumeBase(BaseModel):
    volume_id: int
    title: str
    content: str

class VolumeOut(VolumeBase):
    id: int
    content_hash: str
    created_at: datetime

    class Config:
        from_attributes = True

class HealthOut(BaseModel):
    status: str
    backend: str
    database: str
    volume_count: int
    phi: float
    resonance: float
