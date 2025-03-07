# Use official Python image
FROM python:3.13

# Set working directory
WORKDIR /fastapi-tz

# Copy project files
COPY . /fastapi-tz

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 80

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
