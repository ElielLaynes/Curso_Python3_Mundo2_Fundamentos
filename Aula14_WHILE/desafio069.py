
# Crie um programa que leia:

    # Idade de várias pessoas
    # Sexo de várias pessoas

# A cada pessoas cadastrada, o programa deverá perguntar se o usuário quer continuar ou não

# No final mostre

    # Quantas pessoas tem MAIS DE 18 ANOS
    # Quantos HOMENS foram cadastrados
    # Quantas MULHERES tem MENOS de 20 anos

maior_18_anos = homens_cadastrados = mulheres_20_menos = 0    

while True:
    idade = int ( input ( 'Qual sua Idade? ' ) )
    sexo = ' '
    while sexo not in 'MF':
        sexo = str ( input ( 'Com qual Gênero Você se Identifica? [M/F]:  ' ) ).strip().upper()[0]

    if idade >= 18:
        maior_18_anos += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if idade < 20 and sexo == 'F':
        mulheres_20_menos += 1

    resposta = ' '     
    while resposta not in 'SN':
        resposta = str ( input ( 'Que continuar o Cadastro? [S/N]: ' )).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Total Maiores de 18 anos: {maior_18_anos}')
print(f'Total de Homens Cadatrados: {homens_cadastrados}')
print(f'Mulheres Cadastradas com Menos de 20 Anos: {mulheres_20_menos}')