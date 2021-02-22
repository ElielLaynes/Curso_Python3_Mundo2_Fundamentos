'''
    >>>> ESTRUTURA DE REPETIÇÃO - FOR - <<<<

A estrutura de repetição for é representada da seguinte maneira:

    laço c no intervalo(1, 10):
        passo
    pega

        **** O caracter (c) depois do laço é a variável de controle e pode receber qualquer nome.

representação em python

> com 1 condição de repetição no bloco interno

    for c in range(1, 10):
        passo
    pega

> com 2 condiçoes de repetição no bloco interno

    for c in range(1, 10):
        passo
        pula
    passo
    pega

> laço for e if junto para condiçoes mais complexas

    laço c no intervalo(0, 3):
        se moeda
            pega
        passo
        pula
    passo
    pega

    representação em python

    for c in range(0, 3):
        if moeda:
            pega
        passo
        pula
    passo
    pega
'''



# Exemplos Práticos

for c in range(1, 6):
    print('Oi')
print('fim')


# Imprimir os números do range

for c in range(1, 6):
    print(c)
print('fim')


# Saída ordenada do MAIOR para o MENOR
    # utulizando o -1 para especificar o tipo de iteração, que vai tirar 1 até chegar no fim
for c in range(6, 0, -1):
    print(c)
print('fim')

# Saída pulando um cojunto de elementos
    # Vai contar de 1 até 7(excluindo o 7), pulando de 2 em dois elementos.

for c in range(0, 7, 2):
    print(c)
print('fim')

# Utilizando uma variável com for
    # Usando loop for para contar a entrada de uma variável

num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)
print('fim') 


# Loop FOR com input de dados

inicio = int(input('Início: ')) 
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
print('fim') 


# Loop FOR com input de dados em variável local
    # para repetir uma pergunta

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print(fim)


# lendo um input com loop FOR e adicionando a uma variável

soma = 0

for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
print(f'A soma dos números é: {soma} ')