"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, peso: float, distancia: float) -> float:
        """Calcula o valor do frete com base nos dados do pedido."""
        pass


class FretePorPeso(EstrategiaFrete):
    def __init__(self, valor_por_kg: float = 5.0):
        self.valor_por_kg = valor_por_kg

    def calcular(self, peso: float, distancia: float) -> float:
        # distancia é ignorada nessa estratégia
        return peso * self.valor_por_kg


class FretePorDistancia(EstrategiaFrete):
    def __init__(self, valor_por_km: float = 1.2):
        self.valor_por_km = valor_por_km

    def calcular(self, peso: float, distancia: float) -> float:
        # peso é ignorado nessa estratégia
        return distancia * self.valor_por_km


class FreteFixo(EstrategiaFrete):
    def __init__(self, valor_fixo: float = 30.0):
        self.valor_fixo = valor_fixo

    def calcular(self, peso: float, distancia: float) -> float:
        # ignora peso e distância
        return self.valor_fixo


class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaFrete) -> None:
        self.estrategia = estrategia

    def calcular_frete(self, peso: float, distancia: float) -> float:
        return self.estrategia.calcular(peso, distancia)


def escolher_estrategia(opcao: str) -> EstrategiaFrete:
    if opcao == "1":
        return FretePorPeso()
    elif opcao == "2":
        return FretePorDistancia()
    elif opcao == "3":
        return FreteFixo()
    else:
        raise ValueError("Opção de frete inválida")


if __name__ == "__main__":
    print("=== Cálculo de Frete ===")

    try:
        peso = float(input("Informe o peso total do pedido (em kg): "))
        distancia = float(input("Informe a distância até o cliente (em km): "))

        print("\nEscolha o tipo de frete:")
        print("1 - Frete por peso")
        print("2 - Frete por distância")
        print("3 - Frete fixo")
        opcao = input("Opção: ")

        estrategia = escolher_estrategia(opcao)
        calculadora = CalculadoraFrete(estrategia)

        valor_frete = calculadora.calcular_frete(peso, distancia)
        print(f"\nValor do frete: R$ {valor_frete:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")
