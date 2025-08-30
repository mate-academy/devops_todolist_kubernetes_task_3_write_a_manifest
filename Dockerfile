# Используем официальный Python образ как базовый
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями
COPY src/requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код приложения
COPY src/ .

# Создаем базу данных и выполняем миграции
RUN python manage.py migrate

# Настройка для статических файлов (опционально)
ENV STATIC_ROOT=/app/staticfiles

# Открываем порт 8000
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
