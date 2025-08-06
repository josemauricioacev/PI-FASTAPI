FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./fastapi /app/fastapi

EXPOSE 8000

CMD ["sh", "-c", "uvicorn fastapi.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
