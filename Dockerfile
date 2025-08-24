ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION} AS base
WORKDIR /app

COPY . ./

FROM python:${PYTHON_VERSION}-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY --from=base /app .

RUN pip install --upgrade pip && \
    pip install -r src/requirements.txt && \
    python src/manage.py migrate

ENTRYPOINT ["python", "src/manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

EXPOSE 8080