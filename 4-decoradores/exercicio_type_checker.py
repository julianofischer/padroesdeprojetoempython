"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from functools import wraps


def typecheck(*expected_types):
    """
    Decorator que valida se os argumentos posicionais passados para uma função
    correspondem aos tipos esperados.

    Levanta um TypeError se a quantidade de argumentos for incompatível ou
    se algum argumento tiver um tipo incorreto.
    """

    def decorator(func):
        # Usa @wraps para preservar metadados da função original (como __name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 1. Validação da Quantidade de Argumentos Posicionais
            if len(args) != len(expected_types):
                raise TypeError(
                    f"A função '{func.__name__}' esperava {len(expected_types)} argumentos posicionais, "
                    f"mas recebeu {len(args)}."
                )

            # 2. Validação de Argumentos Nomeados (Conforme Desafio)
            # O desafio foca em argumentos posicionais, então não permite kwargs.
            if kwargs:
                # Opcional: Levantar um erro claro para kwargs, se necessário
                # ou apenas ignorar se a função original souber lidar com eles.
                # Para simplificar e focar no desafio, vamos apenas garantir que
                # a função original não receba argumentos nomeados.
                # Se a função original aceita kwargs, o foco é só no typecheck de args.
                pass

            # 3. Validação dos Tipos dos Argumentos
            for i, (arg_value, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg_value, expected_type):
                    # Encontra o nome do argumento na função original, se possível
                    arg_names = func.__code__.co_varnames
                    arg_name = (
                        arg_names[i]
                        if i < len(arg_names)
                        else f"argumento posicional {i + 1}"
                    )

                    # Levanta um erro informativo
                    raise TypeError(
                        f"Erro de tipo para o {arg_name!r} da função '{func.__name__}'. "
                        f"Esperado: {expected_type.__name__}, Recebido: {type(arg_value).__name__}."
                    )

            # 4. Execução da Função Original se todas as validações passarem
            return func(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == "__main__":
    # ============ Testes ============
    @typecheck(int, str, float)
    def minha_funcao(a, b, c):
        return f"a: {a}, b: {b}, c: {c}"

    print(minha_funcao(10, "teste", 3.14))  # Deve funcionar normalmente
    try:
        print(minha_funcao(10, 20, 3.14))  # Deve levantar TypeError para 'b'
    except TypeError as e:
        print(e)

    try:
        print(
            minha_funcao(10, "teste")
        )  # Deve levantar TypeError por quantidade de args
    except TypeError as e:
        print(e)
