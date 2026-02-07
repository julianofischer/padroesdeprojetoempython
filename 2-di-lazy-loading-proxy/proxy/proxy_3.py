"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Padrão Proxy: fornece um substituto ou marcador para outro objeto
# permitindo controlar o acesso a ele e/ou adicionar uma funcionalidade.
# Vantagens (as próprias aplicações do padrão):
# - Controle de acesso
# - Lazy loading
# - Cache
# - Logging
# Desvantagens:
# - Aumento da complexidade do código
# - Latência adicional na comunicação com o objeto real
# - Pode ser difícil de depurar devido à camada extra (e mascaramento de erros)
# - Cliente pode confundir o proxy com o objeto real


class A:
    @property
    def x(self):
        print("Acessando atributo através de proxy")
        return 10


from functools import partial


def soma(a, b):
    return a + b


plus10 = partial(soma, 10)
r = plus10(5)  # funciona como proxy para soma
print(r)

plus5 = partial(soma, 5)
r = plus5(10)  # funciona como proxy para soma
print(r)
