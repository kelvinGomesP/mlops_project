import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation  # Importa a classe que transformará os dados.

@dataclass
class DataIngestionConfig: # Classe de configuração que define caminhos para salvar os dados.
    train_data_path: str = os.path.join('artefato', "train.csv")
    test_data_path: str = os.path.join('artefato', "test.csv")
    raw_data_path: str = os.path.join('artefato', "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def iniciar_ingestao(self):
        logging.info("Início da ingestão de dados.") #  Loga o início do processo de ingestão.
        try:
        
            df = pd.read_csv('notebook/data/StudentsPerformance.csv')
            logging.info('Dataset lido com sucesso.')

        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Dividindo o dataset em treino e teste.")

            
            train_set, test_set = train_test_split(df, test_size=0.2)

            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestão de dados concluída.")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data, test_data = obj.iniciar_ingestao()

        
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data, test_data)

    except Exception as e:
        logging.error(f"Erro durante o processo de ingestão ou transformação de dados: {e}")
        raise CustomException(e, sys)
