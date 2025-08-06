# Usa una imagen ligera de Python
FROM python:3.11-slim

WORKDIR /app

# Copia solo los requirements primero (para caché de dependencias)
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

EXPOSE 8000

# ¡AQUÍ el cambio!  
# Si Railway está construyendo y ejecutando dentro de fastapi/ (donde está main.py):
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]

# Si por algún motivo Railway toma como raíz el repo (y fastapi/ es subcarpeta),
# entonces usa este (pero solo si da error el de arriba):
# CMD ["sh", "-c", "uvicorn fastapi.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
