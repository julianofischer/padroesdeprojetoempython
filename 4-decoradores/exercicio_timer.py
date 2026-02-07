"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import time


def timer(func):
    """
    Decorator que mede o tempo de execução de uma função.
    Imprime o tempo em segundos com 4 casas decimais.
    """

    def wrapper(*args, **kwargs):
        inicio = time.time()

        # executa a função decorada
        resultado = func(*args, **kwargs)

        fim = time.time()
        tempo = fim - inicio

        print(f"[TIMER] Função '{func.__name__}' executou em {tempo:.4f} segundos")
        return resultado

    return wrapper


# ============ Testes ============


@timer
def tarefa_simples():
    return "Olá, mundo!"


@timer
def tarefa_pesada():
    time.sleep(1.2)
    return "Processamento concluído"


if __name__ == "__main__":
    print(tarefa_simples())
    print(tarefa_pesada())
