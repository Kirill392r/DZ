def log(filename=None):
    """Функция декоратор , который будет автоматически логировать начало и конец выполнения функции"""

    def inner(func):
        """Функция обёртка принимает функцию которую необходимо декорировать"""

        def wrapper(*args, **kwargs):
            """Внутринняя функция"""
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
            except Exception as e:
                error_massage = f"{e} error: тип ошибки. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{error_massage}\n")
                else:
                    print(error_massage)
                    return e
                return result

        return wrapper

    return inner
