ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && \
	pip install -r requirements.txt
RUN python manage.py migrate

ENV PYTHONBUFFERED=1

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver"]

CMD ["0.0.0.0:8080"]
