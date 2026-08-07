FROM python:3.11-slim

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]