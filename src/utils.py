import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("..\\logs\\utils.log", "w", encoding="utf8")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
    Если файл пустой, не найден или содержит не список, возвращает пустой список.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            logger.info("Файла с таким именем не существует или не найден")
            return []

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("Загружены и преобразованны данные файла формата JSON и преобразованны в объект Python")
            return data
        else:
            logger.info("Не корректный тип данных в файле")
            return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Ошибка, тип ошибки: {e}")
        return []
