# Crie um programa que tenha um função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# Situação do aluno (boa ou ruim)


def notas(*num, sit=False):
    """
    -> Programa para analise de notas e situação de vários alunos
    :param num: uma ou mais notas dos alunos, o programa aceita várias notas.
    :param sit: é um valor opcional onde por padrão é setado False e se for True
    mostra a situação do aluno (Ruim, Boa ou Excelente)
    return: dicionário com várias informações sobre as notas e situação dos alunos.
    """
    alunos = {}
    alunos["qte de notas"] = len(num)
    alunos["maior"] = max(num)
    alunos["menor"] = min(num)
    alunos["media"] = sum(num) / (len(num))
    if sit:
        if alunos["media"] >= 8:
            alunos["situação"] = "EXCELENTE"
        elif alunos["media"] >= 6:
            alunos["situação"] = "BOA"
        else:
            alunos["situação"] = "RUIM"
    return alunos


# Programa principal
resp = notas(7.25, 7.75, 9, sit=True)
print(resp)
