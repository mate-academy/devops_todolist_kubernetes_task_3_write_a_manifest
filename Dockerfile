FROM python:3.8

WORKDIR /to-do-app

COPY ./src/requirements.txt ./src/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r ./src/requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/to-do-app/entrypoint.sh"]