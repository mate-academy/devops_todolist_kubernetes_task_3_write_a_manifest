# Use the official Python image as the base image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Installing the requirements with creating the database schema
RUN pip install -r /app/src/requirements.txt && \
    python /app/src/manage.py migrate

# Expose port 8080 to the host
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["python", "/app/src/manage.py", "runserver", "0.0.0.0:8080"]