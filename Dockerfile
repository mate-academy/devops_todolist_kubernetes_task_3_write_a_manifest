FROM python:3.8

WORKDIR /app
COPY . .
COPY src/requirements.txt .
RUN pip install -r src/requirements.txt
COPY . .
EXPOSE 8000

CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
