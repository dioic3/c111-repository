# programa que leia o nome e média de um aluno
# guarde as informações no dicionário
# se a média for maior ou igual a 60
# AP ou RP no if, e guarde no dicionário
# depois mostra as informações do dicionário

nome = str(input("Nome do aluno"))
media = float(input("Média do aluno"))
if media >= 60:
    aprove = 'AP'
else:
    aprove = 'RP'
dados = {'nome': nome, 'média': media, 'resultado':aprove}
print(dados)
