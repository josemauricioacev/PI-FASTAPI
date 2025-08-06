# Usa una imagen ligera de Python
FROM python:3.11-slim

WORKDIR /app

# Copia solo los requirements primero (para aprovechar el caché)
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el resto del código
COPY . .

EXPOSE 8000

# Arranca la app usando el puerto que da Railway (o 8000 en local)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
