ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION} as builder

WORKDIR /devops_todolist
COPY .. .

# Stage 2: Run Stage
FROM python:${PYTHON_VERSION} as run

WORKDIR /devops_todolist

ENV PYTHONUNBUFFERED=1

COPY --from=builder /devops_todolist .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
