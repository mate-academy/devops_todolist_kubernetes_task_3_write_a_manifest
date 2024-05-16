# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run database migrations
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
