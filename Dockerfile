FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app

EXPOSE 8000

CMD ["gunicorn", "todolist.wsgi:application", "--bind", "0.0.0.0:8000"]
