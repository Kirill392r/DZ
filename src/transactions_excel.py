import pandas as pd


def read_transaction_exel(file) -> list[dict]:
    """Функция которая считывает данные с Excel-файла"""
    try:
        if not file:
            return []
        reads = pd.read_excel(file).to_dict(orient="records")
        return reads
    except Exception:
        return []
