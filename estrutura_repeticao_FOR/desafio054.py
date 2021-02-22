
# Crie um Programa que:

    # Leia o ANO DE NASCIMENTO de SETE PESSOAS

    # Quantas pessoas são MAIORES de idade. Considere maior idade = 21 anos

    # Quantas pessoas são MENORES de idade 

import datetime


maior_idade = 0
menor_idade = 0

for ano in range(0, 7):
    ano_nascimento = int ( input ( 'Em que Ano Você Nasceu? ' ) )
    idade = (datetime.date.today().year) - ano_nascimento
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f' MAIOR IDADE: {maior_idade}')
print(f' MENOR IDADE: {menor_idade}')


