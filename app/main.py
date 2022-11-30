from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.routes import router
from app.database import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
