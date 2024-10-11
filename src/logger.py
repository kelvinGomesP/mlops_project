import logging
import os
from datetime import datetime

# 1. Nome do arquivo de log baseado na data e hora atuais.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

# 2. Caminho onde o log será salvo, dentro de uma pasta chamada "logs".
logs_path = os.path.join(os.getcwd(), "logs")  

# 3. Cria o diretório "logs" se não existir
os.makedirs(logs_path, exist_ok=True)

#4. Caminho completo do arquivo de log.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5. Configuração do logger: onde será salvo, o formato da mensagem e o nível de detalhe.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
