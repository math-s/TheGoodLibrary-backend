from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)


handler = Mangum(app, lifespan="off")
