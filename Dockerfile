FROM python:3.10

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

RUN python src/manage.py migrate

EXPOSE 8080

ENTRYPOINT ["python", "src/manage.py", "runserver", "0.0.0.0:8080"]
