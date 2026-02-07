"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class ServicoDePagamento:
    def processar(self, valor):
        print(f"💳 Pagamento de R$ {valor} processado.")


class ServicoDePix:
    def processar(self, valor):
        print(f"⚡ Pagamento via PIX de R$ {valor} processado.")


# --- Simple Factory ---
# cria instâncias de classes relacionadas
# o cliente pede, a Factory decide como criar
def criar_servico_pagamento(tipo):
    if tipo == "cartao":
        return ServicoDePagamento()
    elif tipo == "pix":
        return ServicoDePix()
    else:
        raise ValueError("Tipo de pagamento inválido")


class FabricaDePagamento:
    @staticmethod
    def criar(tipo):
        if tipo == "cartao":
            return ServicoDePagamento()
        elif tipo == "pix":
            return ServicoDePix()
        else:
            raise ValueError("Tipo de pagamento inválido")


# --- Uso ---
class ServicoDePedido:
    def __init__(self, tipo_pagamento):
        self.pagamento = FabricaDePagamento.criar(tipo_pagamento)

    def finalizar_pedido(self, total):
        self.pagamento.processar(total)


# Teste
pedido = ServicoDePedido("pix")
pedido.finalizar_pedido(200)


# Uso:
pagamento = FabricaDePagamento.criar("pix")

# Benefícios
# - centralização da criação
# - baixo acoplamento
# - melhor testabilidade
# - adicionar novos tipos é mais previsível

# Limitação
# - Ainda não é totalmente extensível (é preciso editar a fábrica)
