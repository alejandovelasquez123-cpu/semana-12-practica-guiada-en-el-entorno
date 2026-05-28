from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]

print("=" * 70)
print("DIAGNOSTICO DEL ENTORNO - SEMANA 12")
print("=" * 70)
print(f"Python: {sys.version.split()[0]}")
print(f"Sistema operativo: {platform.system()} {platform.release()}")
print(f"Carpeta del proyecto: {ROOT}")

carpetas = ["data", "src", "docs", "outputs", "ejercicios_estudiante"]
print("\nRevision de carpetas:")
for nombre in carpetas:
    ruta = ROOT / nombre
    estado = "OK" if ruta.exists() else "FALTA"
    print(f"- {nombre}: {estado}")

archivo_base = ROOT / "data" / "produccion_finca.csv"
print("\nArchivo de datos base:")
print(f"- {archivo_base.name}: {'OK' if archivo_base.exists() else 'FALTA'}")

print("\nComando sugerido para continuar:")
print("python src/main.py")
print("=" * 70)
