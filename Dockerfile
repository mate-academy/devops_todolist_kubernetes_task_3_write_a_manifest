ARG PYTHON_VERSION=3.12-slim

# BUILD STAGE ======================================
FROM python:${PYTHON_VERSION} AS build

WORKDIR /app

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install the application dependencies
COPY src/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# RUN STAGE =======================================
FROM python:${PYTHON_VERSION} AS run

WORKDIR /app

# Ensure python finds the virtual environment
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=build /opt/venv /opt/venv

# Copy in the source code
COPY src/accounts/ ./accounts/
COPY src/api/ ./api/
COPY src/lists/ ./lists/
COPY src/todolist/ ./todolist/
COPY src/manage.py ./

EXPOSE 8080

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]