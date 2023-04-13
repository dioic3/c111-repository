# Crie uma lista preenchida com os 5 primeiros
# colocados do Campeonato

# Criação da Lista
colocados = ['Barcelona','França','Alemanha','Brasil','México']
print(colocados)
# mostrar os 3 primeiros colocados
print("Os três primeiros colocados da lista:")
print(colocados[0:3])

# mostrar os ultimos colocados
print("Os 2 ultimos colocados:")
print(colocados[3:5])

#Uma lista com os tims em ordem alfabética
print("Os times em ordem alfabética:")
colocados.sort()
print(colocados)

# A posição que barcelona está na tabela
print("Posição que barcelona está na tabela:")
print(colocados.index("Barcelona"))