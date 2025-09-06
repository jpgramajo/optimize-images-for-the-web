import os
import sys
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')

def process_image(input_path, output_path, quality):
    try:
        with Image.open(input_path) as img:
            # Convertir imágenes con paleta a RGBA si tienen transparencia
            if img.mode == "P":
                img = img.convert("RGBA")
            # Convertir a RGB solo si no tiene transparencia
            elif img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Guardar en WebP manteniendo transparencia si existe
            img.save(output_path, "WEBP", quality=quality)
            print(f"Procesada: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error procesando {input_path}: {e}")

def compress_images(input_folder, quality):
    tasks = []
    output_root = os.path.join(input_folder, "output_webp")

    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith(valid_extensions):
                    input_path = os.path.join(root, file)
                    rel_path = os.path.relpath(root, input_folder)
                    output_path = os.path.join(output_root, rel_path, os.path.splitext(file)[0] + ".webp")
                    tasks.append(executor.submit(process_image, input_path, output_path, quality))

        for _ in as_completed(tasks):
            pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python compress_to_webp.py <folder> <quality 0-100>")
        sys.exit(1)

    folder = sys.argv[1]
    try:
        quality = int(sys.argv[2])
        if not (0 <= quality <= 100):
            raise ValueError
    except ValueError:
        print("El parámetro de calidad debe ser un número entre 0 y 100")
        sys.exit(1)

    compress_images(folder, quality)
    print("¡Todas las imágenes fueron procesadas!")

