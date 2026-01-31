# Use the official Python image as the base image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY src/requirements.txt .

# Копіюємо файл залежностей та встановлюємо їх
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files of the project
COPY src/ .

# Expose port 8080 to the host
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8080"]


