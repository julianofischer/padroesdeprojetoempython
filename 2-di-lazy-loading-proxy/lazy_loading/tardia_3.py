"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")  # lazy por padrão

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

# Populando o banco de dados


with Session(engine) as session:
    author = Author(name="Machado de Assis")
    author.books = [Book(title="Dom Casmurro"), Book(title="Memórias Póstumas")]
    session.add(author)
    session.commit()

with Session(engine) as session:
    a = session.query(Author).first()
    print("Autor carregado — livros ainda não.")
    print(a.__dict__)  # <-- livros ainda não foram carregados
    print(a.books)  # <-- SQL é executado aqui (lazy load)
    print(a.__dict__)


# Inicialização tardia (lazy loading)
# Vantagens: economiza recursos, melhora performance inicial
# Desvantagens:
#  - complexidade adicional no código
#  - múltiplas idas ao banco de dados
#  - pode causar atrasos inesperados (latência) quando os dados são finalmente carregados
#  - mais difícil de depurar, pois o carregamento dos dados é adiado
