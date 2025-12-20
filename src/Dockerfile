FROM python:3.8

WORKDIR /app
COPY . .

# Install app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

# Set the entry point to bash for testing purposes
ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

