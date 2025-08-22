FROM python:3.11-slim

# Ставимо системні залежності
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && rm -rf /var/lib/apt/lists/*

# Робоча папка
WORKDIR /app

# Копіюємо requirements.txt і ставимо Python-залежності
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо увесь код у контейнер
COPY src/ .

# Відкриваємо порт
EXPOSE 8000

# Запуск: міграції + сервер
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
