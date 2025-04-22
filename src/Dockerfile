
FROM python:3.8-slim AS build

WORKDIR /app


COPY requirements.txt .
COPY . .


RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]