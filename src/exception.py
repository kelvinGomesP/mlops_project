import sys
from src.logger import logging  


# 1. Função para detalhar a mensagem de erro.
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() # 2. Captura os detalhes do erro.
    file_name = exc_tb.tb_frame.f_code.co_filename # 3. Nome do arquivo onde o erro ocorreu.
    line_number = exc_tb.tb_lineno # 4. Linha do erro.
    error_message = f"Erro ocorrido no script [{file_name}] na linha [{line_number}]: {str(error)}"
    return error_message # 5. Formata a mensagem de erro.

# 6. Classe customizada de exceção.
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
       
        self.error_message = error_message_detail(error_message, error_detail)  # 7. Formata a mensagem
        logging.error(self.error_message)  # 8. Registra o erro no arquivo de log.
    
    def __str__(self):
        return self.error_message

# Exemplo de uso
'''
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)
'''
