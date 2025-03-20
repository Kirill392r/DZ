import pandas as pd


def read_transaction_exel(file) -> list[dict]:
    """Функция которая считывает данные с Excel файла"""
    try:
        if not file:
            return []
        transaction_list = []
        reads = pd.read_excel(file)
        for index, row in reads.iterrows():
            transaction_list.append(row.to_dict())
        return transaction_list
    except Exception:
        return []
