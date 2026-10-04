ARG PYTHON_VERSION=3.13.2

FROM python:${PYTHON_VERSION} AS base

WORKDIR /app

ADD todolist-arch.tar ./

FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY --from=base /app .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py migrate

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]