# Crie um programa que tenha uma funcao fatorial() que receba dois parâmetros:
# O primeiro indica o número a ser calculado e o outro chamado show, que será um valor
# lógico (opcional) indincando se será mostrado ou não na tela o pocesso do calculo fatorial.


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número digitado
    :param num : O número a ser calculado.
    :param show: (opcional) Se True mostra o calculo do fatorial.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f"{c} x ", end="")
            else:
                print(f"{c} = ", end="")
        f *= c
    return f


# Programa principal
n = int(input("Digite o número: "))
print(f"{fatorial(n, True)}")
