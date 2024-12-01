# Use the official Python image as the base image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY .. .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port 8080 to the host
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
