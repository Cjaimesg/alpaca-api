import configparser
import alpaca_trade_api as tradeapi
import os

# Cargar el archivo de configuración
config = configparser.ConfigParser()

# Configuración para leer el archivo
config = configparser.ConfigParser()

# Ruta del archivo
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

# Leer el archivo con manejo de errores
try:
    config.read(config_path)
    if not config.sections():
        raise FileNotFoundError(f"El archivo '{config_path}' está vacío o no es válido.")
    if 'alpaca' not in config:
        raise KeyError("La sección [alpaca] no se encuentra en el archivo config.ini.")
except Exception as e:
    print(f"Error al leer el archivo de configuración: {e}")
    exit(1)

# Ahora puedes acceder a las claves
API_KEY = config['alpaca']['API_KEY']
SECRET_KEY = config['alpaca']['SECRET_KEY']
BASE_URL = config['alpaca']['BASE_URL']

# Inicializa la conexión a la API de Alpaca
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Ejemplo: Enviar una orden de compra
symbol = "AAPL"
quantity = 1
order_type = "market"
time_in_force = "gtc"

try:
    order = api.submit_order(
        symbol=symbol,
        qty=quantity,
        side="buy",
        type=order_type,
        time_in_force=time_in_force
    )
    print(f"Orden enviada con éxito: {order}")
except Exception as e:
    print(f"Error al enviar la orden: {e}")
