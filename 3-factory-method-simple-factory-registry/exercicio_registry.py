"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ==============================
#   REGISTRO GLOBAL
# ==============================

REGISTRO_COMANDOS = {}


def registrar_comando(nome, classe_comando):
    """
    Registra uma classe de comando no registro global.

    nome: string usada pelo usuário, ex.: "somar"
    classe_comando: a classe que implementa o comando
    """
    REGISTRO_COMANDOS[nome] = classe_comando


# ==============================
#   COMANDOS
# ==============================


class ComandoSomar:
    def executar(self, a, b):
        resultado = a + b
        print(f"[SOMAR] {a} + {b} = {resultado}")
        return resultado


class ComandoSubtrair:
    def executar(self, a, b):
        resultado = a - b
        print(f"[SUBTRAIR] {a} - {b} = {resultado}")
        return resultado


class ComandoMultiplicar:
    def executar(self, a, b):
        resultado = a * b
        print(f"[MULTIPLICAR] {a} * {b} = {resultado}")
        return resultado


# ==============================
#   REGISTRO DOS COMANDOS
# ==============================

registrar_comando("somar", ComandoSomar)
registrar_comando("subtrair", ComandoSubtrair)
registrar_comando("multiplicar", ComandoMultiplicar)


# ==============================
#   CLIENTE
# ==============================

if __name__ == "__main__":
    print("=== Sistema de Comandos com Registry ===")
    print("Comandos disponíveis:", ", ".join(REGISTRO_COMANDOS.keys()))

    comando_escolhido = input("Digite o comando: ").strip().lower()

    if comando_escolhido not in REGISTRO_COMANDOS:
        print("Comando inválido!")
        exit(1)

    try:
        a = float(input("Digite valor A: "))
        b = float(input("Digite valor B: "))
    except ValueError:
        print("Valores inválidos!")
        exit(1)

    ClasseComando = REGISTRO_COMANDOS[comando_escolhido]
    comando = ClasseComando()

    comando.executar(a, b)
