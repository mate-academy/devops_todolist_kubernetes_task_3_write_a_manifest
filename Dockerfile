FROM python:3.8

WORKDIR /app

COPY ./src .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
