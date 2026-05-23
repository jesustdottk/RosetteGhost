# RosetteGhost (v1.0.0)
Un potente script independiente de Python que simula el efecto de **patrón de roseta (halftone)**, característico de las impresiones de periódicos y cómics clásicos.

**RosetteGhost** transforma imágenes digitales en composiciones de puntos de color (Cian, Magenta, Amarillo y Negro) con los ángulos de trama precisos para recrear esa estética física y táctil de la imprenta analógica.

---

## ✨ Características (v1.0.0)
- **Script Standalone Soberano:** Procesamiento por terminal usando Python y Pillow.
- **Simulación CMYK Real:** Descompone la imagen en canales CMYK y aplica tramas de semitonos independientes.
- **Ángulos de Trama Tradicionales:** Configurado con los ángulos estándar para maximizar el efecto roseta y minimizar el moiré indeseado (C: 15°, M: 75°, Y: 0°, K: 45°).
- **Tres niveles de detalle:** **Fino**, **Medio** y **Grueso** (ajusta el tamaño del punto/LPI).
- **Look Analógico:** Incluye opciones para ruido de papel y sangrado de tinta sutil.
- **No destructivo:** Genera una nueva imagen sin alterar el archivo original.

---

## 📂 Estructura del Proyecto
- src/standalone_filter.py: El núcleo del proyecto. Script de Python para uso desde terminal.

---

## 📦 Instalación y Uso

### Requisitos
- Python 3.x
- Librerías: `Pillow`, `numpy`
  `powershell
  pip install Pillow numpy
  `

### Uso
Navega a la carpeta del proyecto y ejecuta el script pasando la ruta de tu imagen:

**Uso Básico (Medio):**
`powershell
python src/standalone_filter.py "ruta/a/imagen.jpg"
`

**Uso Avanzado (Tamaño de punto):**
`powershell
# Efecto de puntos grandes (estilo pop art/cómic)
python src/standalone_filter.py "ruta/a/imagen.jpg" -s grueso

# Efecto de puntos finos (estilo periódico de alta calidad)
python src/standalone_filter.py "ruta/a/imagen.jpg" -s fino
`

**Ayuda:**
`powershell
python src/standalone_filter.py --help
`

---

## 📚 ¿Cómo funciona?
El efecto emula el proceso de cuatricromía (CMYK):
1. **Conversión de Espacio de Color:** La imagen se convierte de RGB a CMYK.
2. **Tramado de Semitonos (Halftoning):** Cada canal se convierte en una matriz de puntos cuyo tamaño varía según la intensidad del color original.
3. **Rotación de Trama:** Cada canal se rota a un ángulo específico para generar el patrón de "roseta" cuando se superponen.
4. **Composición:** Los canales se vuelven a mezclar y se añade una textura de papel opcional.

---

## 📝 Licencia
Este proyecto está bajo la **Elastic License 2.0 (ELv2)**.

---

## 🤝 Créditos
Creado por @jesustdottk + Compa Gemini. Forjado en la República Soberana de ATLAS.
