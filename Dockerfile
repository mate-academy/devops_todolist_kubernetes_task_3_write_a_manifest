ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

WORKDIR /app/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]