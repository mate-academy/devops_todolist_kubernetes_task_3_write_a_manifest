FROM python:3.8

ENV PYTHONDONTWRITEBYCODE=1

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8080

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8080
