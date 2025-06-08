import random
import time
import sys


def main() -> int:
    """Simula una tarea que puede fallar aleatoriamente."""
    print("[main] Ejecutando tarea principal...")
    time.sleep(1)
    if random.random() < 0.5:
        print("[main] Tarea principal completada correctamente.")
        return 0
    else:
        print("[main] Ocurrio un fallo en la tarea principal.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
