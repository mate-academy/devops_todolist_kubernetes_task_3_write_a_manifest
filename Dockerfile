ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION} as builder

WORKDIR /src
COPY src .

FROM python:${PYTHON_VERSION} as run

WORKDIR /src

ENV PYTHONUNBUFFERED=1

COPY --from=builder /src .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
