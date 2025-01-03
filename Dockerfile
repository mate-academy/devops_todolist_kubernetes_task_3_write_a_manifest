# Build stage.
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION} AS base
WORKDIR /devops_todolist_kubernetes_task_3_write_a_manifest

COPY . ./

# Runtime stage
FROM python:${PYTHON_VERSION}-slim
WORKDIR /devops_todolist_kubernetes_task_3_write_a_manifest/src

# Set an environment variable for the runtime.
ENV PYTHONUNBUFFERED=1

# Copy the built application and installed dependencies from the build stage.
COPY --from=base /devops_todolist_kubernetes_task_3_write_a_manifest /devops_todolist_kubernetes_task_3_write_a_manifest
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py migrate

# Expose port 8080 to the host.
EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "runserver"]
CMD ["0.0.0.0:8080"]
