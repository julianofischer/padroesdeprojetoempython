"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# decorators com parâmetros


def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(vezes):
                print(f"[{i + 1}]:", end=" ")
                func(*args, **kwargs)

        return wrapper

    return decorator


@repetir(5)
def imprime():
    print("Executando função...")


imprime()


# Açúcar sintático para:
def diz_ola():
    print("Olá!")


decorador = repetir(3)
diz_ola = decorador(diz_ola)
diz_ola()


@decorador
def say_hello():
    print("Hello!")


say_hello()
