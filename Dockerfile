FROM python:3.10-slim

WORKDIR /app/src
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src/ /app/src
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



