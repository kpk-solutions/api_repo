import sys
from loguru import logger

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from lineage_process import full_lineage
logger.remove()
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{extra[service]}</cyan> | <level>{message}</level>",
    colorize=True
)
logger = logger.bind(service="job-service")

app = FastAPI()

# Allow requests from your frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://localhost:8000"] for safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Job(BaseModel):
    name: str
    description: str

jobs_db = []

@app.post("/job/", response_model=Job)
def create_job(job:Job):
    jobs_db.append(job)
    return job

@app.get("/lineage/{job_name}")
async def get_lineage(job_name: str):
    logger.info('Calling lineage logic')
    lineage = full_lineage(job_name)
    logger.info(f'Lineage data: {lineage}')
    logger.info('Returning the response')
    return lineage