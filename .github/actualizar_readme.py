"""Reescribe la sección "Versión actual" del README con la última versión publicada.

Se ejecuta en GitHub Actions. Toma las versiones de la API de GitHub (comando `gh`)
o de un archivo JSON si se pasa su ruta como argumento (sirve para probarlo).
"""

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
INICIO, FIN = "<!-- VERSION:INICIO -->", "<!-- VERSION:FIN -->"
MESES = (
    "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre"
).split()
SISTEMAS = [(".exe", "Windows", "0078D4"), (".apk", "Android", "34A853")]
SIN_VERSIONES = (
    "## Versión actual\n\n"
    "Todavía no hay instaladores publicados. "
    "Cuando salga la primera versión, los enlaces van a aparecer acá."
)


def leer_versiones() -> list[dict]:
    if len(sys.argv) > 1:
        return json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    salida = subprocess.run(
        ["gh", "api", "repos/{owner}/{repo}/releases?per_page=30"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return json.loads(salida.stdout)


def fecha(iso: str) -> str:
    d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def numero(v: dict) -> str:
    return v["tag_name"].removeprefix("v")


def clave(v: dict) -> tuple[int, ...]:
    """Orden por número de versión: 0.10.0 es más nueva que 0.9.0."""
    return tuple(int(n) for n in re.findall(r"\d+", numero(v))[:3])


def tamano(octetos: int) -> str:
    return f"{octetos / 1024 / 1024:.1f} MB".replace(".", ",")


def seccion(versiones: list[dict]) -> str:
    publicadas = [v for v in versiones if not v["draft"] and not v["prerelease"]]
    if not publicadas:
        return SIN_VERSIONES
    publicadas.sort(key=clave, reverse=True)
    actual = publicadas[0]
    partes = [
        "## Versión actual",
        f"**{numero(actual)}**, publicada el {fecha(actual['published_at'])}.",
    ]

    filas = [
        f"| {sistema} | [{a['name']}]({a['browser_download_url']}) | {tamano(a['size'])} |"
        for extension, sistema, _ in SISTEMAS
        for a in actual["assets"]
        if a["name"].lower().endswith(extension)
    ]
    botones = [
        f"[![Descargar para {sistema}]"
        f"(https://img.shields.io/badge/Descargar_para-{sistema}-{color}?style=for-the-badge&labelColor=172036)]"
        f"({a['browser_download_url']})"
        for extension, sistema, color in SISTEMAS
        for a in actual["assets"]
        if a["name"].lower().endswith(extension)
    ]
    if filas:
        partes.append("\n".join(botones))
        partes.append("\n".join(["| Sistema | Descarga | Tamaño |", "| --- | --- | --- |", *filas]))

    # Las notas no pueden romper las marcas ni los títulos del README.
    notas = (actual["body"] or "").replace("<!--", "").replace("-->", "").replace("\r", "").strip()
    notas = re.sub(r"^(#{1,6})\s+(.+)$", r"**\2**", notas, flags=re.MULTILINE)
    if notas:
        partes.append(f"### Novedades\n\n{notas}")

    if len(publicadas) > 1:
        partes.append(
            "### Versiones anteriores\n\n"
            + "\n".join(
                f"- [{numero(v)}]({v['html_url']}), {fecha(v['published_at'])}" for v in publicadas[1:6]
            )
        )
    return "\n\n".join(partes)


def main() -> None:
    texto = README.read_text(encoding="utf-8")
    if texto.count(INICIO) != 1 or texto.count(FIN) != 1:
        sys.exit("El README tiene que tener una sola vez cada marca VERSION:INICIO y VERSION:FIN.")
    antes, resto = texto.split(INICIO)
    despues = resto.split(FIN)[1]
    README.write_text(
        f"{antes}{INICIO}\n{seccion(leer_versiones())}\n{FIN}{despues}", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
