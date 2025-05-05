from fastapi import FastAPI
from app.job_scraper import get_job_data
from app.db import save_to_db
from app.utils import format_job_data
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get-jobs/{skill}")
async def get_jobs(skill: str, pages: int = 1):
    job_data = get_job_data(skill, pages)
    formatted_data = format_job_data(job_data)
    save_to_db(formatted_data)
    return JSONResponse(content=formatted_data)

@app.get("/job-demand-trend/{skill}")
async def job_trend(skill: str):
    # Logic to fetch and display job demand trend
    return {"fig": "trend_figure_data"}  # Replace with actual trend data
