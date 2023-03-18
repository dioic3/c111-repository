# Variaveis são caracterizadas como espaços de memória para armazenar informações
# para declarar algumas variaveis do python pode usar o operador "="
# O python é uma linguagem de tipagem dinâmica onde o próprio interpretador infere o tipo de dado
# Exemplos
idade = 30
nome = 'Vincent'
peso = 83.5
print(nome,idade,peso)
# Para solicitar alguma informação pode usar usar uma variavél para receber as informações
# Exemplo:
nome1 = input("Qual é o seu nome?") # será guardado no formato de texto, mas pode-se transforma-lo em um tipo
# especifico e dados.

# Tipos de dados:
# int -> representa os números inteiros
# float -> representa os números reais
# bool -> representa somente dois valores, o true e false.
# str -> representa as palavras

# Observação: para qual é o tipo de uma determinada variavél em Python, pode digitar:
print(int(idade))

# Para apresentar uma variavel int, float ou qualquer tipo numa entrada de dados pode usar:
num = int(input('Entre com um número'))

# Operadore Airtméticos -> são classificados por soma, subtração, divisão, igualdade, potenciação, divisão inteira e
# resto da divisão

## Tabela
# + -> soma
# - -> subtração
# * -> multiplicação
# / -> divisão
# == -> igualdade
# ** -> potenciação
# // -> divisão inteira
# % -> resto da divisão

# Módulos e Pacotes do Python
# as formas de importar uma biblioteca do python seria
# import novaBibliotca -> importa todas as funcionalidades/
# from novaBibliotca import partedaNovaBiblioteca -> importa apenas uma recurso especifico

# Cadeia de Caracteres -> Qualquer conteúdo colocado dentro de '' ou "" é chamado de string (Str), mas ao criar uma string
# o python organiza dentro da memória dando um indice para cada um de seus caracteres.

var[6] #captura a letra W da nossa string
var[:5] #captura a palavra Hello
var[6:11] #captura a palavra World (inclusive 6 e 11)
var[6:] # também captura a palavra word
var[0:10:2] #mostra HloWrd( ou seja, pula de 2 em 2)
var[6::2] #mostra Wl(dentro da palavra World, pula de 3 em 3)

len(var) # retorna o numero de caracteres em uma string
var.count('o') # conta o número de o's da nossa palavra
var.count('l',0,5) #conta quantos l's tem dentro de Hello
var.find('lo') #indica a posição de onde começa lo
var.replace('World','Python') #retorna true se a palavra World estiver dentro da palavra var
var.upper() #troca todas as letras para MAIUSCULAS
var.lower() #troca todas as letras para minusculas
var.split() #quebra a frase em partes

# Estrutura de Decisão -> podem ser caractericas como blocos de comandos que mudam o fluxo de execução
# de um software dependendo do resultado de uma variável ou de uma condição

if idade < 18:
    print('Pi')
elif idade > 18:
    print('deu certo')
else:
    print('wii')

# é importante que a identação do if-else seja bem feita porque deixa o código organizado e todo comando
# dentro o if else vai executar dependendo do resultado da condição
# nem sempre o if precisa do else, então podemos usar o elif para adicionar mais condições

# LAÇOS DE REPETIÇÃO -: Podemos usar um loop para executar o mesmo bloco de código enquanto uma condição é atendida.
# a sintaxe do for é:
for c in range(condiçãoInicial, condiçãoFinal):
    # meus comandos

# a sintaxa do while seria:
while condição:
    #meus comandos