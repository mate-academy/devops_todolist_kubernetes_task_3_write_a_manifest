ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# 1. Copy requirements
COPY requirements.txt .

# 2. Install dependencies globally inside image
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of project files
COPY . .

# 4. Use an entrypoint
ENTRYPOINT ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8080"]