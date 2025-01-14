from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(path, "a") as log_file:
                log_file.write(
                    f"Дата вызова функции: {current_time}\n"
                    f"Имя функции: {old_function.__name__}\n"
                    f"Аргументы функции: {args}, {kwargs}\n"
                )
                result = old_function(*args, **kwargs)
                log_file.write(
                    f"Возвращаемое значение функции: {result}\n" f'{"*" * 40}\n\n'
                )
            return result

        return new_function

    return __logger
