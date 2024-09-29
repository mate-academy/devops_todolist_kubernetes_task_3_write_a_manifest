ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}

# Set the working directory
WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r src/requirements.txt

EXPOSE 8081

# Run database migrations and start the Django application
ENTRYPOINT ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8081"]
