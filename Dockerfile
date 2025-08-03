# Use a slim Python image for a smaller container.
FROM python:3.11-slim

# Set the working directory.
WORKDIR /app

# Copy and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY . .

# Expose the port.
EXPOSE 8000

# Command to run the application with Gunicorn.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "main:app"]
