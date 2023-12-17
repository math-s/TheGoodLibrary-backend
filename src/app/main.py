from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers.authors import router as authors_router
from mangum import Mangum
import traceback
import logging

logger = logging.getLogger(__name__)

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
app.include_router(authors_router)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"Internal server error: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal server error"})


handler = Mangum(app, lifespan="off")
