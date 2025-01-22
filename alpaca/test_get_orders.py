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

# Obtener y mostrar las órdenes
try:
    orders = api.list_orders(status='all')  # Cambiar 'all' a 'open', 'closed', o 'cancelled' si necesitas filtrar
    if not orders:
        print("No tienes órdenes disponibles.")
    else:
        print("Órdenes:")
        for order in orders:
            print(f"\nID de orden: {order.id}")
            print(f"Símbolo: {order.symbol}")
            print(f"Cantidad: {order.qty}")
            print(f"Tipo de orden: {order.type}")
            print(f"Estado: {order.status}")
            print(f"Precio límite: {order.limit_price if order.limit_price else 'N/A'}")
            print(f"Precio stop: {order.stop_price if order.stop_price else 'N/A'}")
except Exception as e:
    print(f"Error al obtener las órdenes: {e}")
