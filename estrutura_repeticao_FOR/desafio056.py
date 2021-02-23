
# Desenvolva um programa que leia o :

    # Nome, idade e Sexo de 4 pessoas

    # E mostre:

    # A média de idade do grupo

        # Qual é o nome do homem MAIS VELHOR

            # Quantas mulheres tem MENOS DE 20 anos



soma_idade = 0
media_idade = 0

homem_mais_velho = 0
nome_mais_velho = ''

mulher_20 = 0


for p in range(1, 5):
    print(f'---- Pessoa {p} ----')
    nome = str ( input ( 'Qual seu Nome?' ) ).strip()
    idade = int ( input ( 'Qual sua Idade? ' ) )
    sexo = str ( input ( 'Com qual Gênero Você se Identifica? [ M / F ] : ' ) ).strip()
    soma_idade += idade

    if p == 1 and sexo in 'Mm': # Utilizando in para a validação do sexo. Dessa forma não precisa usar os métodos upper() ou lower()
        homem_mais_velho = idade
        nome_mais_velho = nome

    if sexo in 'Mm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher_20 += 1



media_idade = soma_idade / 4
print(f'A média de idade do grupo é: {media_idade}')
print(f'O homem mais velho tem {homem_mais_velho} anos e se chama {nome_mais_velho}')
print(f' São {mulher_20} mulheres com menos de 20 anos.')
