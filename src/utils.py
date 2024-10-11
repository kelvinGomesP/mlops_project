import os
import sys
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging  
import numpy as np
import pandas as pd

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


def evaluate_model(X_train, y_train, X_test, y_test, models):
    """
    Avalia múltiplos modelos com base no R2 score para os conjuntos de treino e teste.
    
    Args:
        X_train: Características de treino.
        y_train: Rótulos de treino.
        X_test: Características de teste.
        y_test: Rótulos de teste.
        models: Dicionário contendo o nome do modelo como chave e a instância do modelo como valor.
    
    Returns:
        report: Dicionário contendo o nome do modelo e o respectivo R2 score no conjunto de teste.
    """
    try:
        report = {}
        for model_name, model in models.items():
            logging.info(f"Avaliando o modelo: {model_name}")
            
            # Treinar o modelo
            model.fit(X_train, y_train)
            
            # Predições
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # Cálculo do R² para treino e teste
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            logging.info(f"Modelo: {model_name}, R² de treino: {train_model_score}, R² de teste: {test_model_score}")

            # Armazenar o score no relatório
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
