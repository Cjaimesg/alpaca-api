import configparser
import os

# Configuración para leer el archivo
config = configparser.ConfigParser()

# Ruta del archivo
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

# Leer el archivo con manejo de errores
try:
    config.read(config_path)
    if not config.sections():
        raise FileNotFoundError(f"[ERROR] El archivo '{config_path}' está vacío o no es válido.")
    if 'alpaca' not in config:
        raise KeyError("[ERROR]La sección [alpaca] no se encuentra en el archivo config.ini.")
except Exception as e:
    print(f"[ERROR] Error al leer el archivo de configuración: {e}")
    exit(1)

# Ahora puedes acceder a las claves
API_KEY = config['alpaca']['API_KEY']
SECRET_KEY = config['alpaca']['SECRET_KEY']
BASE_URL = config['alpaca']['BASE_URL']

if API_KEY and SECRET_KEY and BASE_URL:
    print("[INFO] Configuración cargada con éxito.")
