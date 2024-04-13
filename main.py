import os
import csv
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    """Extrae los datos EXIF de la imagen especificada por image_path."""
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        exif_info = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            exif_info[tag_name] = value
        return exif_info
    else:
        return None

def dict_to_csv(data_dict, csv_filename):
    """Escribe un diccionario a un archivo CSV. Guarda nombres de archivos con o sin datos GPS."""
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Archivo', 'Latitud', 'Longitud', 'Altitud'])  # Encabezados CSV
        for key, value in data_dict.items():
            if value:
                writer.writerow([key] + value.split(';'))
            else:
                writer.writerow([key, 'No data', 'No data', 'No data'])

def read_jpeg_files(directory):
    """Lee todos los archivos JPEG en el directorio y extrae datos EXIF relacionados con la posición."""
    jpeg_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg'))]
    exif_data = {}
    for file_name in jpeg_files:
        image_path = os.path.join(directory, file_name)
        exif_info = get_exif_data(image_path)
        if exif_info and 'GPSInfo' in exif_info:
            gps_info = exif_info['GPSInfo']
            la = f"{gps_info[2][0]};{gps_info[2][1]};{str(gps_info[2][2]).replace('.',',')}"
            lo = f"{gps_info[4][0]};{gps_info[4][1]};{str(gps_info[4][2]).replace('.',',')}"
            alt = str(gps_info[6]).replace('.',',')
            exif_data[file_name] = f"{la};{lo};{alt}"
        else:
            exif_data[file_name] = ''
            print(f"La imagen {file_name} no contiene datos EXIF.")
    dict_to_csv(exif_data, "output.csv")

# Directorio donde se encuentran las imágenes JPEG
directory = "."
read_jpeg_files(directory)
