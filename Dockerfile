FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r src/requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8080"]
