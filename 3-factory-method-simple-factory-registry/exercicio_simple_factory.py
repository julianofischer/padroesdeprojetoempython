"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class NotificacaoEmail:
    def enviar(self, msg):
        print(f"[EMAIL] Enviando mensagem: {msg}")


class NotificacaoSMS:
    def enviar(self, msg):
        print(f"[SMS] Enviando mensagem: {msg}")


class NotificacaoPush:
    def enviar(self, msg):
        print(f"[PUSH] Enviando mensagem: {msg}")


def criar_notificacao(tipo):
    """
    Função Simple Factory.
    Retorna uma instância de uma classe de notificação
    com base no tipo informado.
    """

    tipo = tipo.lower()  # permite "Email", "EMAIL", etc.

    if tipo == "email":
        return NotificacaoEmail()
    elif tipo == "sms":
        return NotificacaoSMS()
    elif tipo == "push":
        return NotificacaoPush()
    else:
        raise ValueError(f"Tipo de notificação inválido: {tipo}")


if __name__ == "__main__":
    # Exemplos de uso

    notif1 = criar_notificacao("email")
    notif1.enviar("Bem-vindo ao sistema!")

    notif2 = criar_notificacao("sms")
    notif2.enviar("Seu código de verificação é 1234.")

    notif3 = criar_notificacao("push")
    notif3.enviar("Você recebeu uma nova mensagem!")

    # Testando tipo inválido
    try:
        notif4 = criar_notificacao("fax")
    except ValueError as e:
        print("Erro:", e)
