FROM python:3.8.10-slim

WORKDIR /job-service

COPY ./job-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into /job-service
COPY ./job-service/ .

# Expose port 8000 to communicate with the host machine
EXPOSE 8001

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]