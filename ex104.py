# Crie um programa que tenha a função leiaInt()
# Vai funcionar de forma semelhante a funcao input() do Python porém,
# Fará a validação para aceitar apenas um valor numérico. Ex: n = leiaInt("Digite um n: ")


def leiaInt(msg):
    ok = False  # criando uma flag com o padrão False
    valor = 0  # criando uma variável valor com o valor 0
    while True:
        n = str(
            input(msg)
        )  # criando uma variável n que recebe o que foi digitado pelo usuário
        if n.isnumeric():  # validando se o valor recebido é um número
            valor = int(n)
            ok = True  # caso seja um número e tenha sido convertido a inteiro, a flag passa a ser True
        else:
            print(
                "\033[0;31mERRO! Digite um valor inteiro válido!\033[m"
            )  # caso não seja um valor inteiro, é exibido uma mensagem de erro ao usuário
        if ok:
            break
    return valor


# Programa principal
num = leiaInt("Digite o numero: ")
print(f"Você acabou de digitar o número {num}")
