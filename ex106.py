# Criar um mini sistema que utiliza o interactive help do python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra FIM, o programa se encerrará.
# Use cores no terminal.


def minisis():
    while True:
        print("\033[1;33m~" * 30)
        print("\033[1;34mSISTEMA DE AJUDA PyHELP\033[m")
        print("\033[1;33m~" * 30)
        resp = str(input("função ou biblioteca: "))
        if resp.lower() == "fim":
            break
        print("\033[1;35m")
        help(resp)
        print("\033[m")

    print("\033[1;31mFIM DO PROGRAMA!\033[m")


minisis()
