import json
from pathlib import Path
from typing import Any, Dict, List


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
    Если файл пустой, не найден или содержит не список, возвращает пустой список.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
