ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY ./src .

RUN pip install -r requirements.txt && \
    python manage.py migrate

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
