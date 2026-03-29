ARG PYTHON_VERSION=3.12


FROM python:${PYTHON_VERSION}-slim
LABEL authors="Ivan"
WORKDIR /todoapp
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]