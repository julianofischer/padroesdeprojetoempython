"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Dinamicamente agregar funcionalidades adicionais à objetos
# Uma alternativa flexível ao uso de subclasses para extensão de funcionalidades


def somar(a, b):
    return a + b


def dividir(a, b):
    return a / b


# e se quisermos adicionar logs?
def somar_com_log(a, b):
    resultado = a + b
    print(f"Somando {a} + {b} = {resultado}")
    return resultado


# ou ainda
def somar_com_log_2(a, b):
    resultado = somar(a, b)
    print(f"Somando {a} + {b} = {resultado}")
    return resultado


# Repetição de código, difícil de manter
def dividir_com_log(a, b):
    resultado = a / b
    print(f"Dividindo {a} / {b} = {resultado}")
    return resultado


def adicionar_log(func):
    def wrapper(a, b):
        resultado = func(a, b)
        print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
        return resultado

    return wrapper


somar_com_log2 = adicionar_log(somar)
dividir_com_log2 = adicionar_log(dividir)

resultado1 = somar_com_log2(3, 5)
resultado2 = dividir_com_log2(10, 2)
