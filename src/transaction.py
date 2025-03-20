import csv


def read_transaction_csv(file: str) -> list[dict]:
    """Функция которая считывает данные с csv файла"""
    transaction_list = []
    try:
        with open(file, encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transaction_list.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return transaction_list
