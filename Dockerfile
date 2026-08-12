

FROM python:3.8

WORKDIR /app

COPY app.py .
COPY docker-logo.png .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]