ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION} AS builder

WORKDIR /app

COPY . .

FROM python:${PYTHON_VERSION} as run

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /app .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
