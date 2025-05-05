FROM python:3.8.10-slim

WORKDIR /app

COPY  requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into /skill-demand-analyzer
COPY ./app /app

# Expose port 8000 to communicate with the host machine
EXPOSE 8002

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]