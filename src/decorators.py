def log(filename=None):
    """Функция декоратор , который будет автоматически логировать начало и конец выполнения функции"""
    def wrapper(func):
        """Функция обёртка принимает функцию которую необходимо декорировать"""
        def inner(*args, **kwargs):
            """Внутринняя функция"""
            try:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__}, Inputs: {', '.join(map(str, args))}, {kwargs}\n")
                else:
                    print(f"Запуск функции {func.__name__}, Inputs: {', '.join(map(str, args))}, {kwargs}\n")
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
            except Exception as e:
                error_massage = f"{e} error: тип ошибки. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{error_massage}\n")
                else:
                    print(error_massage)
            return result
        return inner
    return wrapper
