FROM python:3.8

WORKDIR /app

copy src/ .
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]