# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /server2_app

# Copy current files into the container
COPY . .

# Install Flask (and other dependencies if needed)
RUN pip install --no-cache-dir Flask

# Expose port 8002 for Flask app
EXPOSE 8002

# Run the Flask app
CMD ["python", "app.py"]


