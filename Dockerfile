ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION} as builder

WORKDIR /app
COPY . .

FROM python:${PYTHON_VERSION} as run

WORKDIR /app

COPY --from=builder /app .

RUN pip install --upgrade pip && \
    pip install -r /app/src/requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python /app/src/manage.py migrate && python /app/src/manage.py runserver 0.0.0.0:8080"]