import sys
from src.logger import logging  

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Erro ocorrido no script [{file_name}] na linha [{line_number}]: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
       
        self.error_message = error_message_detail(error_message, error_detail)
        logging.error(self.error_message)  # Loga o erro automaticamente
    
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
