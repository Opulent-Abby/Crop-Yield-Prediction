# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /workspace

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /workspace

# Expose ports for API and Streamlit
EXPOSE 8000
EXPOSE 8501

# Default command (start nothing, use docker-compose to run specific services)
CMD ["/bin/bash"]
