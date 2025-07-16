# Use a slim Python 3.11 image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy only requirements first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache

# Copy the rest of the project files
COPY scripts/ ./scripts/
COPY db/ ./db/
COPY data/ ./data/

# Set default command
CMD ["python", "scripts/load_data.py"]
