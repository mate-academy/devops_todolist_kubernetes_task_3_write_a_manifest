FROM python:3.13-alpine
WORKDIR /app
COPY src/ /app/
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
