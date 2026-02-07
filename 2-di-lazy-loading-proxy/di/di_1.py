"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Injeção de Dependência


class EmailService:
    def send(self, msg: str):
        print(f"Enviando email: {msg}")


class UserNotifier:
    def __init__(self):
        self.email = EmailService()  # <- acoplado

    def notify(self, user: str):
        self.email.send(f"Olá, {user}!")


# Difícil de testar
# Rígido (e se eu quiser trocar a implementação?)
# Forte acoplamento (UserNotifier conhece a implementação)
