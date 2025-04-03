FROM python:3.11

WORKDIR /app

COPY src/ ./

RUN pip install --no-cache-dir -r requirements.txt

#RUN python manage.py migrate

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]