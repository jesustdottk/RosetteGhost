# RosetteGhost TODO

## Próximas Mejoras (v1.x)
- [ ] **Textura de Papel:** Añadir una opción para aplicar una textura de papel de periódico (crema, granulado) de fondo.
- [x] **Simulación de Ganancia de Punto:** Implementar un efecto donde el punto se expande ligeramente al "absorberse" por el papel. (v2.2.0)
- [ ] **Moiré Estilizado:** Opción para forzar ángulos incorrectos y generar patrones de moiré artísticos.
- [ ] **Tramas Estocásticas:** Añadir modo de trama FM (estocástica) en lugar de AM (semitonos tradicionales).
- [ ] **Exportación Separada:** Opción para guardar cada canal (C, M, Y, K) como archivos independientes para procesos de serigrafía o diseño.
- [x] **Optimización:** Migrar el loop de dibujo de círculos a operaciones de matrices directas en Numpy para mayor velocidad. (v2.4.0)

## Mantenimiento
- [x] Crear set de imágenes de ejemplo en la carpeta `examples/`. (Generadas muestras con diferentes granos y dot gain)
- [ ] Validar compatibilidad con imágenes CMYK nativas de entrada.
