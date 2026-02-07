"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import threading
from singleton1_3 import Singleton

N_THREADS = 100

ids = set()


def create_instance():
    BARRIER = threading.Barrier(N_THREADS)
    instance = Singleton()
    ids.add(id(instance))


def main():
    global ids
    ids = set()
    threads = []
    # Cria N_THREADS threads que tentam criar instâncias do Singleton
    for _ in range(N_THREADS):
        thread = threading.Thread(target=create_instance)
        threads.append(thread)

    # Inicia todas as threads
    for thread in threads:
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    r = 1
    while len(ids) <= 1:
        Singleton._instancia = None
        main()
        r = r + 1
    print(f"Parou na execução: {r} com {len(ids)} instâncias")
