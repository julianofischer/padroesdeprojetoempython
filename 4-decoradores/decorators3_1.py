"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Decorators como classes


class ComLog:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print(f"Executando {self.func.__name__} ({a}, {b})")
        resultado = self.func(a, b)
        print(f"Resultado: {resultado}")
        return resultado


@ComLog
def somar(a, b):
    return a + b


# somar(3, 5) é equivalente a ComLog(somar)(3, 5)
resultado = somar(3, 5)
print("Resultado final:", resultado)


# Açúcar sintático para decorators de classe
# somar = ComLog(somar)


class Repetir:
    def __init__(self, vezes):
        self.vezes = vezes

    def __call__(self, func):
        def wrapper(*args, **kwargs):  # Por que passamos *args e **kwargs aqui?
            for i in range(self.vezes):
                print(f"[{i + 1}]:", end=" ")
                func(*args, **kwargs)

        return wrapper


# Açúcar sintático para decorators de classe com argumentos
# somar = Repetir(3)(somar)


@Repetir(5)
def imprime():
    print("Executando função...")


# imprime() # Equivalente a Repetir(3)(imprime)()
decorador = Repetir(2)
imprime = decorador(imprime)
imprime()

imprime()
