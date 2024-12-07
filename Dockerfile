# Use the official Python image as base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy application code into the container 
COPY .. .

RUN pip install --upgrade pip && \
    pip install -r src/requirements.txt

# Map container port to host
EXPOSE 8080:8080

ENTRYPOINT [ "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080" ]
