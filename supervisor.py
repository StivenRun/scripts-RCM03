import subprocess
from pathlib import Path


MAIN_SCRIPT = Path(__file__).with_name("script_main.py")
FALLBACK_SCRIPT = Path(__file__).with_name("script_fallback.py")


def run_script(path: Path) -> int:
    """Ejecuta un script y retorna su codigo de salida."""
    print(f"[supervisor] Ejecutando {path}...")
    result = subprocess.run(["python", str(path)])
    print(f"[supervisor] Codigo de salida de {path}: {result.returncode}")
    return result.returncode


def main() -> None:
    code = run_script(MAIN_SCRIPT)
    if code != 0:
        print("[supervisor] El script principal fallo. Lanzando fallback...")
        run_script(FALLBACK_SCRIPT)
    else:
        print("[supervisor] Ejecucion completada correctamente.")


if __name__ == "__main__":
    main()
