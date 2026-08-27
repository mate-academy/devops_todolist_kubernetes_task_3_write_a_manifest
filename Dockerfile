FROM python:3.11

WORKDIR /app

COPY src/. .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]

