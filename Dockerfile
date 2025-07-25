FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 8080

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8080"]