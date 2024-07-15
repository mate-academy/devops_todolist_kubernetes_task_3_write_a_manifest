ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION} as builder

WORKDIR /app

COPY . .

FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY --from=builder /app .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]

