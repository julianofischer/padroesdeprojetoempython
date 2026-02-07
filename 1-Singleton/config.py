"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class Config:
    _instance = None  # atributo de classe para armazenar a única instância

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # se ainda não existe instância
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, debug=False, database_url="localhost", database_port=5432):
        # Evitar reexecutar init se a instância já existe
        if not hasattr(self, "_initialized"):
            self.debug = debug
            self.database_url = database_url
            self.database_port = database_port
            self._initialized = True  # marca que já inicializou


if __name__ == "__main__":
    config1 = Config(debug=True)
    config2 = Config()

    print("Mesma instância? ", id(config1) == id(config2))

    # alterando valor em uma variável
    config1.debug = False

    # verificando se reflete na outra
    print("A alteração refletiu? ", config2.debug == False)

    config3 = Config(database_url="abc", database_port=1234)
    config4 = Config(database_port=9999)
    print(config3.database_url, config4.database_url)  # ambos devem ser "abc"
    print(config3.database_port, config4.database_port)  # ambos devem ser "abc"
