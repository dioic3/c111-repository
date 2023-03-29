# Crie dois conjuntos, um ara cada loja
# idenficar quais modelos de smartphones cada loja vende (x)
# mostre quais modelos no total o usuário terá opção
# de comprar se visitá-las
# quais modelos se encontram em ambas as lojas

visitar = str(input('Digite loja 1 ou loja 2 para verificar quais smartphones cada uma delas vendem:'))
iguais = str(input('Digite iguais para encontrar os modelos iguais que as lojas vendem'))
#identificação dos modelos
loja1 = {'Iphone 6','Iphone 7','Iphone 8','Iphone 9','Iphone 10', 'Samsung S22 Plus','Samsung S21'}
loja2 = {'Iphone 10', 'Iphone 8','Samsung S21'}

if visitar == "loja 1":
    print(loja1)
    print("Quantidade de opções:")
    print(len(loja1))
elif visitar == "loja 2":
    print(loja2)
    print("Quantidade de opções:")
    print(len(loja2))
if iguais == "iguais":
    print(loja1 & loja2)