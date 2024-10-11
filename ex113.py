# Crie um programa que tenha a função leiaInt()
# Vai funcionar de forma semelhante a funcao input() do Python porém,
# Fará a validação para aceitar apenas um valor numérico. Ex: n = leiaInt("Digite um n: ")


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um valor inteiro válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\nO usuário não digitou um valor!")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um valor real válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\nO usuário não digitou um valor!")
            return 0
        else:
            return n

# Programa principal
num = leiaInt("Digite o numero inteiro: ")
num2 = leiafloat("Digite um número real: ")
print(f"Você acabou de digitar o número {num} e o número {num2}")
