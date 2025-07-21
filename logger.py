import logging

"""
Настраиваем логгер
"""
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

"""Обработка для записи (перезапись файла при запуске
"""
file_handler = logging.FileHandler('logs/app.log', mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
