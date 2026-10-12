# Gebruik een officiële Python runtime die voldoet aan de vereisten
FROM python:3.9-slim

# Stel de werkomgeving in
WORKDIR /app

# Installeer systeemvereisten en afhankelijkheden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de applicatiecode
COPY . .

# Voer database migraties uit tijdens het builden (of via entrypoint)
RUN python manage.py migrate

# Exposeer de poort waarop Django draait
EXPOSE 8000

# Start de Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
