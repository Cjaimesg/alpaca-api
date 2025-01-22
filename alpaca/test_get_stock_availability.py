import alpaca_trade_api as tradeapi
import configparser
import os
import csv

# Cargar el archivo de configuración
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

try:
    config.read(config_path)
    if not config.sections():
        raise FileNotFoundError(f"El archivo '{config_path}' está vacío o no es válido.")
    if 'alpaca' not in config:
        raise KeyError("La sección [alpaca] no se encuentra en el archivo config.ini.")
except Exception as e:
    print(f"Error al leer el archivo de configuración: {e}")
    exit(1)

# Credenciales de Alpaca
API_KEY = config['alpaca']['API_KEY']
SECRET_KEY = config['alpaca']['SECRET_KEY']
BASE_URL = config['alpaca']['BASE_URL']

# Inicializa la conexión a la API de Alpaca
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Obtener listado de todas las acciones disponibles
try:
    assets = api.list_assets()
    
    # Nombre del archivo CSV
    csv_file_path = os.path.join(os.path.dirname(__file__), 'acciones_disponibles.csv')
    
    # Crear y escribir en el CSV
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Encabezado de la columna
        csv_writer.writerow(["Symbol", "Name", "Status"])
        
        # Escribir cada acción en una fila
        for asset in assets:
            csv_writer.writerow([asset.symbol, asset.name, asset.status])
    
    print(f"Listado de acciones guardado en: {csv_file_path}")
except Exception as e:
    print(f"Error al obtener el listado de acciones: {e}")
