from config import TRANSACTION_PATH_CSV, TRANSACTION_PATH_JSON, TRANSACTION_PATH_XLSX
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search import filter_operations
from src.transaction import read_transaction_csv
from src.transactions_excel import read_transaction_exel
from src.utils import read_transactions


def main():
    while True:
        try:
            print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
            print("Выберите необходимый пункт меню:")

            while True:
                try:
                    choice = input(
                        "1. Получить информацию о транзакциях из JSON-файла\n"
                        "2. Получить информацию о транзакциях из CSV-файла\n"
                        "3. Получить информацию о транзакциях из XLSX-файла\n"
                        "4. Выход\n"
                        "Ваш выбор: "
                    ).strip()

                    if not choice:
                        print("Ошибка: введите число от 1 до 4")
                        continue

                    input_info = int(choice)

                    if input_info == 1:
                        transactions = read_transactions(TRANSACTION_PATH_JSON)
                        break
                    elif input_info == 2:
                        transactions = read_transaction_csv(TRANSACTION_PATH_CSV)
                        break
                    elif input_info == 3:
                        transactions = read_transaction_exel(TRANSACTION_PATH_XLSX)
                        break
                    elif input_info == 4:
                        print("Завершение работы программы...")
                        return
                    else:
                        print("Ошибка: введите число от 1 до 4")
                except ValueError:
                    print("Ошибка: введите число от 1 до 4")

            while True:
                input_status = (
                    input("\nВведите статус (EXECUTED, CANCELED, PENDING)\n" "Или 'назад' для возврата в меню: ")
                    .strip()
                    .upper()
                )

                if not input_status:
                    print("Ошибка: статус не может быть пустым")
                    continue

                if input_status == "НАЗАД":
                    break

                if input_status not in ["EXECUTED", "CANCELED", "PENDING"]:
                    print(f"Ошибка: статус '{input_status}' недоступен")
                    continue

                filtered_data = filter_by_state(transactions, input_status)
                print(f"\nНайдено операций: {len(filtered_data)}")

                if not filtered_data:
                    print("Нет транзакций с выбранным статусом.")
                    continue

                while True:
                    sort_choice = input("\nОтсортировать по дате? (да/нет): ").strip().lower()
                    if sort_choice in ["да", "нет"]:
                        break
                    print("Ошибка: введите 'да' или 'нет'")

                if sort_choice == "да":
                    while True:
                        order = input("По возрастанию или по убыванию? ").strip().lower()
                        if order in ["по возрастанию", "по убыванию"]:
                            break
                        print("Ошибка: введите 'по возрастанию' или 'по убыванию'")

                    reverse = order == "по убыванию"
                    filtered_data = sort_by_date(filtered_data, reverse)

                while True:
                    rub_choice = input("\nТолько рублевые транзакции? (да/нет): ").strip().lower()
                    if rub_choice in ["да", "нет"]:
                        break
                    print("Ошибка: введите 'да' или 'нет'")

                if rub_choice == "да":
                    filtered_data = [
                        t
                        for t in filtered_data
                        if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
                    ]
                    print(f"Осталось рублевых транзакций: {len(filtered_data)}")

                while True:
                    word_choice = input("\nФильтровать по слову в описании? (да/нет): ").strip().lower()
                    if word_choice in ["да", "нет"]:
                        break
                    print("Ошибка: введите 'да' или 'нет'")

                if word_choice == "да":
                    keyword = input("Введите слово для поиска: ").strip().lower()
                    if not keyword:
                        print("Ошибка: слово для поиска не может быть пустым")
                    else:
                        filtered_data = filter_operations(filtered_data, keyword)
                        print(f"Найдено транзакций по слову '{keyword}': {len(filtered_data)}")

                print("\n=== Результаты ===")
                if not filtered_data:
                    print("Нет транзакций по вашим критериям.")
                else:
                    for i, transaction in enumerate(filtered_data, 1):
                        date = transaction.get("date", "Нет даты")
                        desc = transaction.get("description", "Без описания")

                        from_acc = transaction.get("from", "")
                        masked_from = ""
                        if from_acc:
                            try:
                                digits = "".join(c for c in from_acc if c.isdigit())
                                if "счет" in from_acc.lower():
                                    masked_from = from_acc.split()[0] + " " + get_mask_account(digits)
                                else:
                                    masked_from = " ".join(from_acc.split()[:-1]) + " " + get_mask_card_number(digits)
                            except Exception as e:
                                print(f"Ошибка маскировки номера отправителя: {e}")
                                masked_from = from_acc

                        to_acc = transaction.get("to", "")
                        masked_to = ""
                        if to_acc:
                            try:
                                digits = "".join(c for c in to_acc if c.isdigit())
                                if "счет" in to_acc.lower():
                                    masked_to = to_acc.split()[0] + " " + get_mask_account(digits)
                                else:
                                    masked_to = " ".join(to_acc.split()[:-1]) + " " + get_mask_card_number(digits)
                            except Exception as e:
                                print(f"Ошибка маскировки номера получателя: {e}")
                                masked_to = to_acc

                        amount = transaction.get("operationAmount", {}).get("amount", "?")
                        currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "")

                        print(f"\n{i}. {date} {desc}")
                        if masked_from:
                            print(f"   Откуда: {masked_from}")
                        print(f"   Куда: {masked_to}")
                        print(f"   Сумма: {amount} {currency}")

                    print(f"\nВсего операций: {len(filtered_data)}")

                while True:
                    continue_choice = input("\nПродолжить работу? (да/нет): ").strip().lower()
                    if continue_choice in ["да", "нет"]:
                        break
                    print("Ошибка: введите 'да' или 'нет'")

                if continue_choice == "нет":
                    break

        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            print("Возврат в главное меню...\n")


if __name__ == "__main__":
    main()
