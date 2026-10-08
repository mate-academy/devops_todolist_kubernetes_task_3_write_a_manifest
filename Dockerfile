# Використовуємо офіційний легкий образ Python
FROM python:3.10-slim

# Налаштовуємо змінні оточення, щоб Python не створював .pyc файли і не буферизував логи
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проєкту в контейнер
COPY . /app/

# Виконуємо міграції та відкриваємо порт
EXPOSE 8000

# Запускаємо вбудований сервер Django (для продакшну краще gunicorn, але для таски підходить)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
