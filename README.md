# Sistema de ejecucion periodica de scripts

Este repositorio contiene un entorno Docker que ejecuta `script_main.py` cada
cinco minutos. Si la tarea principal falla, automaticamente se ejecuta
`script_fallback.py` gracias a `supervisor.py`.

## Archivos

- `script_main.py`: tarea principal que falla de forma aleatoria.
- `script_fallback.py`: tarea de respaldo.
- `supervisor.py`: ejecuta `script_main.py` y si detecta error lanza el
  fallback.
- `supervisord.conf`: configuracion de supervisord que lanza el supervisor cada
  cinco minutos mediante un bucle `while true`.
- `Dockerfile`: construye la imagen e inicia supervisord.
- `docker-compose.yml`: define el servicio Docker con reinicio automatico.
- `.dockerignore`: excluye archivos innecesarios al crear la imagen.

## Uso rapido

1. Construir y ejecutar con docker compose:

```bash
docker-compose up --build
```

2. Detener el servicio con `Ctrl+C` y eliminar contenedores:

```bash
docker-compose down
```
