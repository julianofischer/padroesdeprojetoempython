"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod


# =============================
#   PRODUTO ABSTRATO
# =============================
class Document(ABC):
    def __init__(self, title):
        self.title = title
        self.content = ""

    @abstractmethod
    def generate_content(self):
        pass

    @abstractmethod
    def export(self):
        pass


# =============================
#   PRODUTOS CONCRETOS
# =============================
class PlainTextDocument(Document):
    def generate_content(self):
        self.content = f"Documento Texto: {self.title}\nConteúdo simples."
        print("[PlainText] Conteúdo gerado!")

    def export(self):
        print(f"[PlainText] Exportando TXT:\n{self.content}\n")


class HTMLDocument(Document):
    def generate_content(self):
        self.content = f"<html><h1>{self.title}</h1><p>Conteúdo em HTML.</p></html>"
        print("[HTML] Conteúdo gerado!")

    def export(self):
        print(f"[HTML] Exportando HTML:\n{self.content}\n")


class CSVDocument(Document):
    def generate_content(self):
        self.content = "coluna1,coluna2,coluna3\nvalor1,valor2,valor3"
        print("[CSV] Conteúdo gerado!")

    def export(self):
        print(f"[CSV] Exportando CSV:\n{self.content}\n")


# =============================
#   CREATOR ABSTRATO
# =============================
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self, title):
        pass

    def export_document(self, title):
        """
        Fluxo padronizado para todos os tipos de documento:
        1. Criar documento (Factory Method)
        2. Gerar conteúdo
        3. Exportar
        """
        print("[Creator] Iniciando fluxo de criação/exportação...")
        doc = self.create_document(title)
        doc.generate_content()
        doc.export()
        return doc


# =============================
#   CREATORS CONCRETOS
# =============================
class PlainTextDocumentCreator(DocumentCreator):
    def create_document(self, title):
        print("[Creator] Criando documento TXT...")
        return PlainTextDocument(title)


class HTMLDocumentCreator(DocumentCreator):
    def create_document(self, title):
        print("[Creator] Criando documento HTML...")
        return HTMLDocument(title)


class CSVDocumentCreator(DocumentCreator):
    def create_document(self, title):
        print("[Creator] Criando documento CSV...")
        return CSVDocument(title)


# =============================
#   CLIENTE
# =============================
def escolher_creator(tipo: str) -> DocumentCreator:
    tipo = tipo.lower()
    if tipo == "txt":
        return PlainTextDocumentCreator()
    elif tipo == "html":
        return HTMLDocumentCreator()
    elif tipo == "csv":
        return CSVDocumentCreator()
    else:
        raise ValueError(f"Tipo inválido: {tipo}")


if __name__ == "__main__":
    print("=== Sistema de Documentos (Factory Method) ===")
    tipo = input("Digite o tipo de documento (txt/html/csv): ")

    try:
        creator = escolher_creator(tipo)
        creator.export_document("Relatório de Vendas")
    except ValueError as e:
        print("Erro:", e)
