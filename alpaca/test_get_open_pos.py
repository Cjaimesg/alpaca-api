import configparser
import alpaca_trade_api as tradeapi
import os

# Cargar el archivo de configuración
config = configparser.ConfigParser()

# Ruta del archivo de configuración
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

# Acceder a las claves del archivo de configuración
API_KEY = config['alpaca']['API_KEY']
SECRET_KEY = config['alpaca']['SECRET_KEY']
BASE_URL = config['alpaca']['BASE_URL']

# Inicializa la conexión a la API de Alpaca
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Obtener y mostrar las posiciones abiertas
try:
    positions = api.list_positions()
    if not positions:
        print("No tienes posiciones abiertas actualmente.")
    else:
        print("Posiciones abiertas:")
        for position in positions:
            print(f"\nSímbolo: {position.symbol}")
            print(f"Cantidad: {position.qty}")
            print(f"Precio promedio: ${position.avg_entry_price}")
            print(f"Valor de mercado: ${position.market_value}")
            print(f"Ganancia/pérdida no realizada: ${position.unrealized_pl}")
except Exception as e:
    print(f"Error al obtener las posiciones abiertas: {e}")