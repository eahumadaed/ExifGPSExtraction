# Lector de Datos EXIF

Este programa está diseñado para leer imágenes JPEG en un directorio especificado, extraer datos EXIF relevantes (especialmente información de GPS) y guardar estos datos en un archivo CSV.

## Funciones

- `get_exif_data(image_path)`: Extrae los datos EXIF de una imagen dada.
- `dict_to_csv(data_dict, csv_filename)`: Guarda un diccionario de datos en formato CSV.
- `read_jpeg_files(directory)`: Lee todas las imágenes JPEG de un directorio, extrae datos EXIF de GPS y los guarda en un archivo CSV llamado `output.csv`.

## Uso

1. Coloque todas las imágenes JPEG de las cuales desea extraer datos EXIF en el mismo directorio que el script.
2. Ejecute el script. Los resultados se guardarán en `output.csv` en el mismo directorio.