# Imagen base de Python
FROM python:3.11-slim

# Instala supervisord
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Comando por defecto: iniciar supervisord con la configuracion proporcionada
CMD ["supervisord", "-c", "/app/supervisord.conf"]
