FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r src/requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
