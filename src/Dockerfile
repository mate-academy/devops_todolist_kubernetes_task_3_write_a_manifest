# Build stage
FROM python:3.12-slim

WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies and run migrations
RUN pip install -r requirements.txt && python manage.py migrate

# Expose port 8080 to the host
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
