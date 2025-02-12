# Use the official Python image as the base image
FROM python:3.9-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src /app/src

EXPOSE 8080

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8080"]