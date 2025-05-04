# lineage-service/main.py
import sys
from loguru import logger
from fastapi import FastAPI

from lineage_process import full_lineage

logger.remove()
# logger.add(sys.stdout, level="DEBUG", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>", colorize=True)
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{extra[service]}</cyan> | <level>{message}</level>",
    colorize=True
)
logger = logger.bind(service="lineage-service")



app = FastAPI()

@app.get("/lineage/{job_name}")
async def get_lineage(job_name: str):
    logger.info('Calling lineage logic')
    lineage = full_lineage(job_name)
    logger.info(f'Lineage data: {lineage}')
    logger.info('Returning the response')
    return lineage
