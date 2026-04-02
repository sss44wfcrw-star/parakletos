import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers.health import router as health_router
from .routers.volumes import router as volumes_router
from .routers.verify import router as verify_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PARAKLETOS API", version="1.1.0")

frontend_origin = os.getenv("FRONTEND_ORIGIN", "*")
allow_origins = [frontend_origin] if frontend_origin != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(volumes_router)
app.include_router(verify_router)
