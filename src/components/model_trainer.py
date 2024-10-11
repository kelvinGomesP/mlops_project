import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_fit_path = os.path.join("artefato", "modelpkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info("Split de treino e teste iniciado")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoost Regressor": CatBoostRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # Avaliação dos modelos
            model_report = self.evaluate_model(X_train, y_train, X_test, y_test, models)

            # Encontre o melhor modelo com base no score
            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            # Validação do score do melhor modelo
            if best_model_score < 0.6:
                raise CustomException("Modelo ruim: o desempenho é inferior a 0.6 no R².")

            logging.info(f"Melhor modelo encontrado: {best_model_name} com score {best_model_score}")

        except Exception as e:
            raise CustomException(e, sys)

    def evaluate_model(self, X_train, y_train, X_test, y_test, models):
        try:
            report = {}

            for model_name, model in models.items():
                logging.info(f"Treinando e avaliando o modelo: {model_name}")
                
               
                model.fit(X_train, y_train)
                
                
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                
               
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)

                # Armazenar os resultados no relatório
                report[model_name] = test_model_score  # Usando o score de teste para avaliação principal

            return report
        
        except Exception as e:
            raise CustomException(e, sys)
