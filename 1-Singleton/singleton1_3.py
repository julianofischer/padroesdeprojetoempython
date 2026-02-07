"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                # Dupla verificação porque pode ter sido criada
                # enquanto esperava pelo lock
                if cls._instance is None:
                    print("Criando a instância única")
                    cls._instance = super().__new__(cls)
        return cls._instance
