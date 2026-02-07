"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# empilhando decorators


def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(vezes):
                print(f"[{i + 1}]:", end=" ")
                func(*args, **kwargs)

        return wrapper

    return decorator


def adicionar_log(func):
    def wrapper(a, b):
        resultado = func(a, b)
        print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
        return resultado

    return wrapper


@repetir(3)
@adicionar_log
def somar(a, b):
    return a + b


somar(2, 3)
