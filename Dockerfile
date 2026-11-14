FROM python:3.9-slim

WORKDIR /app

COPY src/requirements.txt /app

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

COPY src/ /app

RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]