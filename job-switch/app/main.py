from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.job_scraper import get_job_data
from app.db import save_to_db
from app.utils import format_job_data
from app.logger import logger


app = FastAPI()

@app.get("/get-jobs/{skill}")
async def get_jobs(skill: str, pages: int = 1):
    try:
        job_data = get_job_data(skill, pages)
        logger.info(f"job_data: {job_data}")
        formatted_data = format_job_data(job_data)
        logger.info(f"formatted_data: {formatted_data}")
        save_to_db(formatted_data)
    except Exception as e:
        formatted_data = {"Message": f"{e}"}
    return JSONResponse(content=formatted_data)

@app.get("/job-demand-trend/{skill}")
async def job_trend(skill: str):
    # Logic to fetch and display job demand trend
    return {"fig": "trend_figure_data"}  # Replace with actual trend data
