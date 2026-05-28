# Use a lightweight Python base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install the dependencies your code needs
RUN pip install --no-cache-dir fastapi uvicorn requests

# Copy your files: index.html, logic.py, main.py
COPY . .

# FastAPI runs on port 8000 by default in your main.py
EXPOSE 8000

# Start the application
CMD ["python", "main.py"]
