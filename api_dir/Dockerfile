FROM python:3.8.10-slim

WORKDIR /lineage-json-export

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code folder into the container
COPY ./lineage-json-export .

# Expose port 8000 to communicate with the host machine
EXPOSE 8000

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
