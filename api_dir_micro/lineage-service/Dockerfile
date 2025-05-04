FROM python:3.8.10-slim

WORKDIR /lineage-service

COPY ./lineage-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code from the subdir
COPY ./lineage-service/ .

# Expose port 8000 to communicate with the host machine
EXPOSE 8000

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

