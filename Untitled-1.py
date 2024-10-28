
def log_function_call(func):
    def wrapper(*args):
        print(f'Вызвана функция {func.__name__} с аргументами: {args}')
        result = func(*args)
        return result
    return wrapper

@log_function_call
def summa(a, b):
    return a + b

@log_function_call
def summa2(a, b, c):
    return a + b + c


summa(5, 3)
