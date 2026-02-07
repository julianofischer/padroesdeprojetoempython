"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Closure: função interna lembrar do estado da função externa
# nonlocal: modificar variável da função externa


def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(vezes):  # como a funcao interna lembra do parâmetro vezes?
                print(f"[{i + 1}]:", end=" ")
                func(*args, **kwargs)

        return wrapper

    return decorator


@repetir(5)
def imprime():
    print("Executando função...")


imprime()


def limite(maximo):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal maximo
            if maximo == 0:
                print("Limite de chamadas atingido.")
                return None
            maximo = maximo - 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limite(3)
def diz_ola():
    print("Olá!")


diz_ola()
diz_ola()
diz_ola()
diz_ola()  # essa chamada não deve ser executada
