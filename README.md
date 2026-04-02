# PARAKLETOS Rebuild — Production Ready

This package upgrades the rebuild to a production-ready starter.

## Included
- `backend/seed.py`
- `render.yaml`
- `.env.example`
- pinned backend dependencies
- Postgres-ready database configuration
- configurable CORS via `FRONTEND_ORIGIN`
- static frontend config file

## Local run
### Backend
```bash
cd backend
pip install -r requirements.txt
python seed.py
uvicorn app.main:app --reload
```

### Frontend
Open `frontend/index.html`

## Render deploy
This repo includes a root `render.yaml` so you can deploy the API, static frontend, and managed Postgres from one blueprint file.

## Notes
- Local default DB is SQLite.
- Production should use `DATABASE_URL` from Render Postgres.
- The frontend uses `frontend/config.js` for the API base URL.
