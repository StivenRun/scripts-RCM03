import time


def main() -> int:
    """Script de respaldo que se ejecuta si el script principal falla."""
    print("[fallback] Ejecutando tarea de respaldo...")
    time.sleep(1)
    print("[fallback] Tarea de respaldo completada.")
    return 0


if __name__ == "__main__":
    main()
