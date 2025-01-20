FROM python:3.9-slim

WORKDIR /app

#COPY src/requirements.txt .
RUN pip install -r src/requirements.txt

#COPY . .
COPY src /app/src

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
