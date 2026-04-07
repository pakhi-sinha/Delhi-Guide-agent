# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container (including __init__.py and agent.py)
COPY . .

# Expose the default port (Cloud Run uses 8080 by default)
EXPOSE 8080

# Command to run the Google ADK web development UI
# This will serve the agent interface using the current directory
CMD ["adk", "web", "--port", "8080", "--host", "0.0.0.0"]
