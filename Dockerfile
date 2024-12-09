FROM python:3.8-slim
WORKDIR /app
COPY src/requirements.txt /app/
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]