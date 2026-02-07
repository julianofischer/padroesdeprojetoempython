"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

def repetir(func):
    def wrapper():
        for i in range(3):
            print(f"[{i + 1}]:", end=" ")
            func()

    return wrapper


@repetir
def imprime():
    print("Executando função...")


imprime()

# e se eu quiser repetir com outro número de vezes?
# e se quisermos aplicar mais de um decorator?
