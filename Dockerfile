FROM python:3.10-slim
WORKDIR /devops_todolist_kubernetes_task_3_write_a_manifest
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]