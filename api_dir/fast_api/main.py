from fastapi import FastAPI

app = FastAPI()

@app.get("/lineage/{job_name}")
async def get_lineage(job_name: str):
    lineage = {"upstream": ["job2", "job3"], "downstream": ["job4"]}
    return {job_name: lineage}

import sql_connection

@app.get("/sql/{job_name}")
async def get_db(job_name: str):
    row = sql_connection.connection()
    result = {"row": str(row)}
    return {job_name: result}
