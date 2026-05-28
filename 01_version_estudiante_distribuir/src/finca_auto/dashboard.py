from __future__ import annotations

from datetime import datetime
from pathlib import Path
import json


def _barra(valor: float, maximo: float) -> int:
    if maximo <= 0:
        return 0
    return int((valor / maximo) * 100)


def generar_dashboard(resultado: dict, registros: list[dict], carpeta_dashboard: Path) -> Path:
    carpeta_dashboard.mkdir(parents=True, exist_ok=True)
    ruta = carpeta_dashboard / "index.html"
    max_leche = max(r["leche_litros"] for r in registros)

    filas = []
    for r in registros:
        ancho = _barra(r["leche_litros"], max_leche)
        filas.append(f"""
        <tr>
          <td>{r['fecha']}</td>
          <td>{r['dia']}</td>
          <td>{r['leche_litros']}</td>
          <td><div class='bar'><span style='width:{ancho}%'></span></div></td>
          <td>{r['maiz_kg']}</td>
          <td>{r['lluvia_mm']}</td>
          <td>{r['responsable']}</td>
        </tr>
        """)

    alertas = "".join(f"<li>{a}</li>" for a in resultado["alertas"]) or "<li>No se generaron alertas.</li>"
    datos_json = json.dumps({"leche": [r["leche_litros"] for r in registros], "dias": [r["dia"] for r in registros]}, ensure_ascii=False)

    html = f"""
<!doctype html>
<html lang='es'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>Dashboard producción rural</title>
  <style>
    :root {{ --azul:#1f4e79; --verde:#1f7a4d; --rojo:#b03a2e; --fondo:#f4f7fb; --texto:#1c2833; }}
    body {{ margin:0; font-family:Segoe UI,Arial,sans-serif; background:var(--fondo); color:var(--texto); }}
    header {{ background:linear-gradient(135deg,var(--azul),#102a43); color:white; padding:34px 7%; }}
    header h1 {{ margin:0; font-size:34px; }}
    header p {{ margin-bottom:0; opacity:.95; }}
    main {{ padding:28px 7%; }}
    .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:18px; }}
    .card {{ background:white; border-radius:18px; padding:22px; box-shadow:0 8px 24px rgba(0,0,0,.08); }}
    .card .label {{ font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:#6b7280; }}
    .card .value {{ font-size:32px; font-weight:800; color:var(--azul); margin-top:10px; }}
    section {{ background:white; margin-top:24px; border-radius:18px; padding:24px; box-shadow:0 8px 24px rgba(0,0,0,.07); }}
    table {{ width:100%; border-collapse:collapse; font-size:14px; }}
    th,td {{ padding:12px; border-bottom:1px solid #e5e7eb; text-align:left; }}
    th {{ background:#eef3f8; color:#183b56; }}
    .bar {{ background:#e5e7eb; height:12px; border-radius:99px; overflow:hidden; min-width:120px; }}
    .bar span {{ display:block; height:100%; background:var(--verde); }}
    li {{ margin:8px 0; }}
    .tag {{ display:inline-block; background:#eafaf1; color:var(--verde); padding:6px 10px; border-radius:99px; font-weight:700; }}
    footer {{ padding:22px 7%; color:#6b7280; }}
  </style>
</head>
<body>
  <header>
    <h1>Dashboard de producción rural</h1>
    <p>Generado automáticamente el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} mediante un script de Python.</p>
  </header>
  <main>
    <div class='cards'>
      <div class='card'><div class='label'>Total leche</div><div class='value'>{resultado['total_leche_litros']} L</div></div>
      <div class='card'><div class='label'>Promedio leche</div><div class='value'>{resultado['promedio_leche_litros']} L</div></div>
      <div class='card'><div class='label'>Total maíz</div><div class='value'>{resultado['total_maiz_kg']} kg</div></div>
      <div class='card'><div class='label'>Alertas</div><div class='value'>{len(resultado['alertas'])}</div></div>
    </div>

    <section>
      <h2>Tendencia</h2>
      <p><span class='tag'>{resultado['tendencia']}</span></p>
    </section>

    <section>
      <h2>Alertas generadas</h2>
      <ul>{alertas}</ul>
    </section>

    <section>
      <h2>Registros válidos</h2>
      <table>
        <thead><tr><th>Fecha</th><th>Día</th><th>Leche</th><th>Visual</th><th>Maíz</th><th>Lluvia</th><th>Responsable</th></tr></thead>
        <tbody>{''.join(filas)}</tbody>
      </table>
    </section>
  </main>
  <footer>
    Datos usados por el dashboard: <script>const datos = {datos_json}; document.write(datos.dias.length + ' registros procesados.');</script>
  </footer>
</body>
</html>
"""
    ruta.write_text(html, encoding="utf-8")
    return ruta
