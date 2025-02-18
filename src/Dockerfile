FROM python:3.8

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python","manage.py","runserver","0.0.0.0:8080"]