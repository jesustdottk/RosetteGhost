import argparse
import numpy as np
from PIL import Image, ImageEnhance, ImageChops, ImageFilter
import os
import sys

def get_euclidean_halftone(channel, angle, cell, dot_gain=0.1, oversample=4):
    """
    Genera un halftone de puntos circulares (Euclidean) con alta fidelidad.
    El oversampling elimina los "triangulitos" y crea puntos redondos reales.
    """
    orig_w, orig_h = channel.size
    
    # 1. Proceso en Super-Resolución
    # Redimensionamos el mapa de intensidad
    chan_high = channel.resize((orig_w * oversample, orig_h * oversample), Image.BICUBIC)
    arr_high = np.array(chan_high)
    h, w = arr_high.shape
    
    # 2. Rotación para el ángulo de la trama
    # Expand=True es vital para no perder esquinas durante la rotación del patrón
    rotated = Image.fromarray(arr_high).rotate(angle, expand=True)
    r_arr = np.array(rotated)
    rw, rh = r_arr.shape
    
    # 3. Lienzo de salida para los puntos
    out = np.zeros_like(r_arr)
    
    # Ajustamos la celda al oversampling
    cell_high = cell * oversample
    
    # 4. Motor de Puntos Euclidianos (Vectorizado con NumPy)
    # Reemplazamos el doble loop por operaciones de matrices
    cell_high = cell * oversample
    
    # Creamos una cuadrícula de coordenadas para toda la imagen rotada
    # y calculamos los centros de cada celda
    y_coords, x_coords = np.indices((rw, rh))
    
    # Centros de las celdas
    center_y = (y_coords // cell_high) * cell_high + (cell_high - 1) / 2.0
    center_x = (x_coords // cell_high) * cell_high + (cell_high - 1) / 2.0
    
    # Distancia de cada píxel a su centro de celda correspondiente
    dist_sq = (x_coords - center_x)**2 + (y_coords - center_y)**2
    
    # Calculamos la intensidad media por celda de forma eficiente
    # Redimensionamos para agrupar por celdas y promediar
    pad_y = (cell_high - rw % cell_high) % cell_high
    pad_x = (cell_high - rh % cell_high) % cell_high
    r_arr_padded = np.pad(r_arr, ((0, pad_y), (0, pad_x)), mode='constant')
    
    # Agrupamos en bloques de celdas
    shape = (r_arr_padded.shape[0] // cell_high, cell_high, 
             r_arr_padded.shape[1] // cell_high, cell_high)
    strides = r_arr_padded.strides
    new_strides = (cell_high * strides[0], strides[0], 
                   cell_high * strides[1], strides[1])
    
    blocks = np.lib.stride_tricks.as_strided(r_arr_padded, shape=shape, strides=new_strides)
    
    # Promedio por bloque (intensidad de la celda)
    cell_means = np.mean(blocks, axis=(1, 3)) / 255.0
    
    # Aplicar Ganancia de Punto a la matriz de promedios
    cell_means = cell_means + (dot_gain * 4.0 * cell_means * (1.0 - cell_means))
    cell_means = np.clip(cell_means, 0.0, 1.0)
    
    # Expandimos los promedios de vuelta al tamaño de la imagen original (sin pad)
    # y calculamos el radio cuadrado necesario para cada píxel
    radii_sq_grid = np.repeat(np.repeat(cell_means, cell_high, axis=0), cell_high, axis=1)
    radii_sq_grid = radii_sq_grid[:rw, :rh] * (cell_high / 2.0)**2 * 1.2
    
    # Generamos los puntos: si la distancia al centro es menor al radio, pintamos blanco
    out = (dist_sq <= radii_sq_grid).astype(np.uint8) * 255

    # 5. Rotar de vuelta y Restaurar Tamaño
    final = Image.fromarray(out).rotate(-angle, expand=True)
    
    # Recorte central preciso
    fw, fh = final.size
    tw, th = orig_w * oversample, orig_h * oversample
    final = final.crop(((fw-tw)/2, (fh-th)/2, (fw+tw)/2, (fh+th)/2))
    
    # El downsampling con LANCZOS crea el antialiasing que le da el look "impreso"
    return final.resize((orig_w, orig_h), Image.LANCZOS)

def apply_fidelity_rosette(input_path, size='fino', weight=0.75, dot_gain=0.1, fmt='jpg', brightness=1.0):
    """
    Motor v2.4.0: Rosette Fidelity + Dual Format + Exposure Control.
    """
    params = {
        'micro': 2,
        'fino': 4,
        'medio': 7,
        'grueso': 12
    }
    cell_size = params.get(size.lower(), params['fino'])
    
    try:
        orig = Image.open(input_path).convert('RGB')
        
        # 0. Redimensión Automática (Límite 600px altura)
        max_h = 600
        curr_w, curr_h = orig.size
        if curr_h > max_h:
            new_h = max_h
            new_w = int((new_h / curr_h) * curr_w)
            print(f"📏 Redimensionando de {curr_w}x{curr_h} a {new_w}x{new_h}...")
            orig = orig.resize((new_w, new_h), Image.LANCZOS)
        
        # 1. Separación CMYK
        cmyk = orig.convert('CMYK')
        c, m, y, k = cmyk.split()
        
        # Ángulos Rosette (Clásicos de Prensa)
        angles = [15, 75, 0, 45]
        
        print(f"🚀 Iniciando Motor de Fidelidad v2.4.0 (Rosette Master)")
        print(f"✨ Forjando puntos circulares ({size.upper()})...")
        print(f"💧 Simulando Ganancia de Punto: {dot_gain*100:.1f}%")
        
        # 2. Generar Tramas Euclidianas
        c_ht = get_euclidean_halftone(c, angles[0], cell_size, dot_gain=dot_gain, oversample=4)
        m_ht = get_euclidean_halftone(m, angles[1], cell_size, dot_gain=dot_gain, oversample=4)
        y_ht = get_euclidean_halftone(y, angles[2], cell_size, dot_gain=dot_gain, oversample=4)
        k_ht = get_euclidean_halftone(k, angles[3], cell_size, dot_gain=dot_gain, oversample=4)
        
        # Recomponer estructura de puntos
        rosette_pure = Image.merge("CMYK", (c_ht, m_ht, y_ht, k_ht)).convert("RGB")
        
        # 3. Fusión de Experiencia
        orig_vibrant = ImageEnhance.Color(orig).enhance(1.2)
        orig_vibrant = ImageEnhance.Contrast(orig_vibrant).enhance(1.1)
        
        final = ImageChops.multiply(orig_vibrant, rosette_pure)
        
        # Control de Brillo / Exposición (v2.4.0)
        if brightness != 1.0:
            final = ImageEnhance.Brightness(final).enhance(brightness)
        
        if weight < 1.0:
            final = Image.blend(orig, final, weight)
            
        # 4. Guardado Inteligente
        ext = fmt.lower()
        output_path = os.path.splitext(input_path)[0] + f"_rosette_{size}.{ext}"
        
        if ext == 'jpg' or ext == 'jpeg':
            final.save(output_path, "JPEG", quality=90, optimize=True)
        else:
            final.save(output_path, "PNG")
            
        return output_path

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    description = """
🌌 Rosette Ghost — Fidelity Engine (v2.4.0)
Look Roseta Real: Puntos Euclidianos, Fusión Perceptiva y Ganancia de Punto.
Adiós a los triangulitos, hola a la imprenta analógica.
    """
    
    epilog = """
Ejemplos de uso:
  python src/standalone_filter.py foto.jpg -s fino -w 0.8
  python src/standalone_filter.py foto.jpg -s medio -g 0.2 -b 1.2

─── dammgo labs ───────────────────────────────────────────
  » Engineering Longevity. Friendship as Code.
  » Forjado con 💙 por @jesustdottk + Compa Gemini.
  » República Soberana de ATLAS.
───────────────────────────────────────────────────────────
    """

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("input", nargs="?", help="Imagen de entrada")
    parser.add_argument("-s", "--size", choices=['micro', 'fino', 'medio', 'grueso'], default='fino', 
                        help="Tamaño del grano (default: fino)")
    parser.add_argument("-w", "--weight", type=float, default=0.75, 
                        help="Fuerza de la trama (0.1 a 1.0, default: 0.75)")
    parser.add_argument("-g", "--gain", type=float, default=0.1, 
                        help="Ganancia de punto (0.0 a 0.5, default: 0.1)")
    parser.add_argument("-f", "--format", choices=['jpg', 'png'], default='jpg', 
                        help="Formato de salida (default: jpg)")
    parser.add_argument("-b", "--brightness", type=float, default=1.0, 
                        help="Brillo/Exposición (default: 1.0, ej: 1.2 para más brillo)")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    
    if not args.input:
        print("Error: Debes especificar una imagen de entrada.")
        sys.exit(1)

    if os.path.exists(args.input):
        print("-" * 40)
        print(f"🚀 Procesando: {os.path.basename(args.input)}")
        print(f"✨ Config: Roseta {args.size.upper()} | Peso: {args.weight} | Ganancia: {args.gain} | Brillo: {args.brightness}")
        print("-" * 40)
        
        out = apply_fidelity_rosette(args.input, args.size, args.weight, args.gain, args.format, args.brightness)
        
        if out:
            print(f"✅ ¡Éxito! Imagen guardada en:")
            print(f"   > {out}")
        print("-" * 40)
    else:
        print(f"❌ Error: El archivo '{args.input}' no existe.")
        sys.exit(1)
