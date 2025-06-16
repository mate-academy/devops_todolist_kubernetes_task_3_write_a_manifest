# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY ./src .
COPY ./src/requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the host
EXPOSE 8000

# Define the command to run the application
ENTRYPOINT ["sh", "-c"]
CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]