# Stage 1: Build Stage
FROM python:3.8 AS builder

# Set the working directory
WORKDIR /app
COPY . .

# Stage 2: Run Stage
FROM python:3.8 AS run

WORKDIR /app

COPY --from=builder /app .

RUN pip install --upgrade pip && \
    pip install -r src/requirements.txt

EXPOSE 8080

# Run database migrations and start the Django application
ENTRYPOINT ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8080"]