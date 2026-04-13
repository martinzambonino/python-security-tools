"""
log_analyzer.py — Detecta patrones de fuerza bruta en logs de acceso sintéticos.

Uso:
    python src/log_analyzer.py --file data/sample_logs.txt --threshold 5

Alcance: Estrictamente educativo. Solo usar con logs propios o sintéticos.
Autor: Martin Sebastian Zambonino Gavela — EPN Ecuador.
"""

import argparse
import re
from collections import Counter
from pathlib import Path


FAILED_LOGIN_PATTERN = re.compile(
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}).*(?:Failed|Invalid|authentication failure)",
    re.IGNORECASE,
)


def analyze_failed_logins(log_path: Path, threshold: int) -> dict[str, int]:
    """Retorna IPs con intentos fallidos >= threshold.

    Args:
        log_path: Ruta al archivo de log a analizar.
        threshold: Número mínimo de intentos fallidos para reportar una IP.

    Returns:
        Diccionario {ip: cantidad_intentos} para IPs que superan el umbral.
    """
    counts: Counter = Counter()

    with log_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                counts[match.group("ip")] += 1

    return {ip: n for ip, n in counts.items() if n >= threshold}


def main() -> None:
    """Punto de entrada principal."""
    parser = argparse.ArgumentParser(
        description="Analiza logs en busca de patrones de fuerza bruta"
    )
    parser.add_argument("--file", required=True, help="Ruta al archivo de log")
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Intentos fallidos mínimos (default: 5)",
    )
    args = parser.parse_args()

    log_path = Path(args.file)
    if not log_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {log_path}")

    suspicious = analyze_failed_logins(log_path, args.threshold)

    if not suspicious:
        print(f"[OK] Ninguna IP supera el umbral de {args.threshold} intentos fallidos.")
        return

    print(f"\n[ALERTA] IPs con >= {args.threshold} intentos fallidos:")
    for ip, count in sorted(suspicious.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ip:<18} {count:>4} intentos")


if __name__ == "__main__":
    main()
