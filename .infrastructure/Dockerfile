ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]