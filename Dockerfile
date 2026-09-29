FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
