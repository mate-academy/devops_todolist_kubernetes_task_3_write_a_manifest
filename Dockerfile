FROM python:3.8-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]