FROM python:3.10-slim

WORKDIR /app/src
COPY src/requirements.txt /app/requirements.txt

# Використовуємо дзеркало та розбиваємо встановлення
RUN pip config set global.index-url https://pypi.org/simple && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app/src
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
