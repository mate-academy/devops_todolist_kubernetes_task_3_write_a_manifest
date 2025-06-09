FROM python:3.14.0b2-alpine3.22
WORKDIR /app
COPY src/requirements.txt .
COPY src/ .
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python manage.py migrate
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]