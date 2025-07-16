# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy files and folders from your local to container
COPY requirements.txt .
COPY scripts/ ./scripts/
COPY data/ ./data/
COPY db/ ./db/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run (you can change to any script later)
CMD ["python", "scripts/load_data.py"]
