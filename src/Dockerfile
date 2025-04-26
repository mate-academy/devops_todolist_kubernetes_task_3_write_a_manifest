FROM python:3.8

WORKDIR /app

COPY manage.py ./
COPY todolist ./todolist
COPY accounts ./accounts
COPY api ./api
COPY lists ./lists
COPY entrypoint.sh ./entrypoint.sh
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x ./entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]