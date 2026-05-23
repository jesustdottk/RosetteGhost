# Contribuir a LenticularGhost

¡Gracias por tu interés en contribuir a este proyecto!  
LenticularGhost es una herramienta independiente en Python para procesamiento de imágenes retro-ópticas.

---

## 🧩 Cómo contribuir

### 1. Haz un fork del repositorio
Crea tu propia copia del proyecto para trabajar en ella.

### 2. Crea una rama para tu cambio
Usa un nombre descriptivo:

```powershell
git checkout -b mejora-algoritmo-ruido
```

### 3. Realiza tus cambios
Asegúrate de que:
- El código esté bien comentado y siga los principios de ATLAS.
- El script mantenga su simplicidad y no añada dependencias pesadas innecesarias.
- No se rompa la interfaz de línea de comandos (CLI) existente.

### 4. Prueba tu cambio
Verifica que el script funcione correctamente:
- Ejecutándolo con diferentes intensidades (`-i`).
- Probando las orientaciones horizontal y vertical (`-d`).
- Verificando la compatibilidad con formatos JPG y PNG.

### 5. Envía un Pull Request
Incluye:
- Descripción clara de la mejora o corrección.
- Ejemplos visuales de "antes y después".
- Referencia a un issue si corresponde.

---

## 🧪 Estilo del código
- Usamos **Pillow** y **NumPy** como base técnica.
- Mantén el código idiomático y limpio.
- Documenta cualquier nuevo parámetro de la CLI.

---

## 📜 Licencia
Al contribuir, aceptas que tu código será publicado bajo la **Elastic License 2.0 (ELv2)**.

---

## 🙌 Gracias
Tu ayuda hace que LenticularGhost sea una herramienta más soberana y potente.
