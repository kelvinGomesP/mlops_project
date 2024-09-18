import logging
import os
from datetime import datetime

# Definindo o arquivo de log com timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
logs_path = os.path.join(os.getcwd(), "logs")  # Diretório de logs separado do arquivo de log

# Cria o diretório de logs se ele não existir
os.makedirs(logs_path, exist_ok=True)

# Caminho completo do arquivo de log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configurações do logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
