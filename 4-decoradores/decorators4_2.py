"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

registry = {}


def registrar(nome):
    def decorator(cls):
        registry[nome] = cls
        return cls

    return decorator


@registrar("pix")
class PagamentoPix:
    pass


# equivalente a
# PagamentoPix = registrar("pix")(PagamentoPix)


@registrar("cartao")
class PagamentoCartao:
    pass


print(registry)
print(registry["pix"])
print(registry["cartao"])
