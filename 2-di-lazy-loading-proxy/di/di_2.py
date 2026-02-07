"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Inversão de Controle
# Quem usa a dependência, não cria a dependência.


# Separação de responsabilidades
# UserNotifier não sabe mais "como" a mensagem é enviada
class UserNotifier:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, user: str):
        self.sender.send(f"Olá, {user}!")
