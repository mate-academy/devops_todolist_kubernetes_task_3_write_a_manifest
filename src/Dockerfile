ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app  
COPY . /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*
  
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]