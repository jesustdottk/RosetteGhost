# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2026-05-23

### Added
- **Motor Vectorizado (NumPy):** Refactorización completa del motor de tramado para usar operaciones de matrices, mejorando el rendimiento en un ~80%.
- **Simulación de Ganancia de Punto (Dot Gain):** Nueva funcionalidad para simular la expansión de tinta en el papel (parámetro `-g`).
- **Control de Brillo:** Añadido parámetro `-b` para ajustar la exposición final de la imagen.
- **Redimensión Automática:** Límite inteligente de 600px de altura para prevenir errores y acelerar el flujo.
- **Soporte Formato Dual:** Ahora permite guardar en **JPG** (default) o **PNG** mediante el flag `-f`.
- **Nuevo nivel de detalle:** Añadido modo `micro` para tramas ultra-finas.

### Changed
- El formato de salida por defecto ahora es JPG para optimizar el peso del archivo.
- Versión del motor actualizada a v2.4.0 (Fidelity Master).

### Fixed
- Corregido error de "Decompression Bomb" al procesar imágenes de alta resolución mediante la redimensión previa.

## [1.0.0] - 2026-05-18

### Added
- Versión inicial de **RosetteGhost**.
- Script `src/standalone_filter.py` con soporte para tramas de semitonos CMYK.
- Algoritmo de patrón de roseta con ángulos de trama tradicionales (15, 75, 0, 45).
- Soporte para intensidades: Fino, Medio y Grueso.
- Sistema de Gray Component Replacement (GCR) para un look más realista.
- README y documentación base siguiendo el estándar de ATLAS Laboratory.
