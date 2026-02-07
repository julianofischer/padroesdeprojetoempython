"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Dinamicamente agregar funcionalidades adicionais à objetos
# Uma alternativa flexível ao uso de subclasses para extensão de funcionalidades
# E o padrão Proxy?
# Proxy é sobre controle de acesso a um objeto, enquanto decoradores são sobre adicionar funcionalidades.


def adicionar_log(func):
    def wrapper(a, b):
        resultado = func(a, b)
        print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
        return resultado

    return wrapper


@adicionar_log
def somar(a, b):
    return a + b


# somar = adicionar_log(somar)


@adicionar_log
def dividir(a, b):
    return a / b


# dividir = adicionar_log(dividir)
somar(3, 5)
dividir(10, 2)
