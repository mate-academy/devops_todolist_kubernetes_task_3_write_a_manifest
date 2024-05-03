FROM python:3.8 as builder

WORKDIR /app

COPY .. .

FROM python:3.8 as run

WORKDIR /app

COPY --from=builder /app .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
