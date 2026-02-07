"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import sys
import logging
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


def main():
    # Exemplos de singleton "à moda Python"
    sys.stdin
    sys.stdout
    sys.stderr

    # None, True, False
    print("None is None: ", None is None)
    print(id(None), id(None))
    print("True is True: ", True is True)
    print(id(True), id(True))
    print("False is False: ", False is False)
    print(id(False), id(False))

    # logging.getLogger()
    log1 = logging.getLogger("meu_log")
    log2 = logging.getLogger("meu_log")
    print("log1 is log2: ", log1 is log2)
    print(id(log1), id(log2))


def test_sqlalchemy_singleton():
    print("-" * 20)
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = scoped_session(sessionmaker(bind=engine))

    session1 = Session()
    session2 = Session()
    print("session1 is session2: ", session1 is session2)
    print(id(session1), id(session2))


if __name__ == "__main__":
    main()
    test_sqlalchemy_singleton()
