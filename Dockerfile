FROM python:3.11-alpine

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

RUN python manage.py migrate

CMD ["sh", "-c", "python src/manage.py migrate --noinput && python src/manage.py runserver 0.0.0.0:8080"]

EXPOSE 8080