FROM python:3.13-alpine
WORKDIR /app
COPY src/ /app/
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
