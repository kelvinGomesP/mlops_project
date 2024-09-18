import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging  


def save_object(file_path, obj):
    try:
        # Verifica se o objeto é válido
        if obj is None:
            raise ValueError("O objeto fornecido é None e não pode ser salvo.")

        # Cria o diretório do arquivo, se ele não existir
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Salva o objeto usando 'dill'
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Objeto salvo com sucesso em: {file_path}")

    except ValueError as ve:
        logging.error(f"Erro de valor: {ve}")
        raise CustomException(ve, sys)

    except Exception as e:
        logging.error(f"Erro ao salvar o objeto: {e}")
        raise CustomException(e, sys)
