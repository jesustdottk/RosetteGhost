# RosetteGhost (v2.4.0)
Un potente script independiente de Python que simula el efecto de **patrón de roseta (halftone)**, característico de las impresiones de periódicos y cómics clásicos. Forjado para la longevidad y la fidelidad analógica.

**RosetteGhost** transforma imágenes digitales en composiciones de puntos de color (CMYK) con ángulos de trama precisos, simulando ahora fenómenos físicos como la ganancia de punto y la absorción de tinta.

---

## ✨ Características (v2.4.0)
- **Motor Vectorizado (NumPy):** Procesamiento ultra rápido mediante operaciones de matrices. Adiós a los loops lentos.
- **Simulación de Ganancia de Punto (Dot Gain):** Controla la expansión de la tinta en el papel para un look más "húmedo" y real.
- **Control de Exposición:** Ajuste de brillo integrado para compensar el oscurecimiento natural del tramado.
- **Redimensión Inteligente:** Ajuste automático de imágenes grandes (límite 600px altura) para optimizar el rendimiento.
- **Formato Dual:** Salida optimizada en **JPG** (default para ligereza) o **PNG** (máxima fidelidad).
- **Ángulos de Trama Tradicionales:** Configurado con los ángulos estándar (C: 15°, M: 75°, Y: 0°, K: 45°).
- **Cuatro niveles de detalle:** **Micro**, **Fino**, **Medio** y **Grueso**.

---

## 📂 Estructura del Proyecto
- `src/standalone_filter.py`: El núcleo del proyecto. Script de Python v2.4.0.
- `examples/`: Galería de muestras procesadas con diferentes configuraciones.

---

## 📦 Instalación y Uso

### Requisitos
- Python 3.x
- Librerías: `Pillow`, `numpy`

```bash
pip install Pillow numpy --break-system-packages
```

### Uso Básico
```bash
# Salida JPG (default) con grano fino
python src/standalone_filter.py "imagen.jpg"
```

### Uso Avanzado (Flags)
| Flag | Descripción | Valores |
| :--- | :--- | :--- |
| `-s` | Tamaño del punto | `micro`, `fino`, `medio`, `grueso` |
| `-g` | Ganancia de punto | `0.0` a `0.5` (default: 0.1) |
| `-b` | Brillo / Exposición | `1.0` (default), `1.2` (más claro) |
| `-f` | Formato de salida | `jpg`, `png` |
| `-w` | Peso del efecto | `0.1` a `1.0` (fusión con original) |

**Ejemplo de look "Periódico Antiguo":**
```bash
python src/standalone_filter.py "foto.jpg" -s medio -g 0.25 -b 1.2
```

**Ejemplo de look "Pop-Art / Cómic":**
```bash
python src/standalone_filter.py "foto.jpg" -s grueso -g 0.1 -w 1.0
```

---

## 📚 ¿Cómo funciona? (Motor Fidelity)
1. **Redimensión:** Si la imagen supera los 600px de altura, se escala para mantener la eficiencia.
2. **Conversión CMYK:** Descomposición real en canales de tinta.
3. **Tramado Euclidiano Vectorizado:** Generación de puntos circulares perfectos usando álgebra de matrices en NumPy.
4. **Fusión de Experiencia:** Se aplica un aumento de contraste y color antes de multiplicar la trama por la imagen original.
5. **Compensación Física:** Se aplica la curva de Ganancia de Punto y el ajuste de brillo final.

---

## 📝 Licencia
Este proyecto está bajo la **Elastic License 2.0 (ELv2)**.

---

## 🤝 Créditos
Creado por @jesustdottk + Compa Gemini.
─── **dammgo labs** ───────────────────────────────────────
  » Engineering Longevity. Friendship as Code.
  » República Soberana de ATLAS.
───────────────────────────────────────────────────────────
