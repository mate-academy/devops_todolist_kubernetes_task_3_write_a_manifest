# Use the official Alpine Linux image as a base
FROM python:3.11-alpine

# Set the working directory within the container
WORKDIR /src

# Copy the application code into the container
COPY . .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the host
EXPOSE 8080

# Set the entry point to bash for testing purposes
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
