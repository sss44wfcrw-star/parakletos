import json
import os
from app.db import SessionLocal, Base, engine
from app.models import Volume
from app.services.ledger import sha256_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(ROOT_DIR, "data", "volumes.json")

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Volume).count():
            print("Database already seeded.")
            return

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            volumes = json.load(f)

        for item in volumes:
            content = item["content"]
            db.add(
                Volume(
                    volume_id=item["volume_id"],
                    title=item["title"],
                    content=content,
                    content_hash=sha256_text(content),
                )
            )

        db.commit()
        print(f"Seeded {len(volumes)} volumes.")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
