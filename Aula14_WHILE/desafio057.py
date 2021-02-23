

# Faça um programa que leia o sexo de uma pessoa

# Só aceite os valores 'M' ou 'F'

# Caso seja outro valor, Peça a digitação novamente até ter um valor correto

sexo = 'M','F'

while sexo != 'M' and sexo != 'F':
    sexo = str ( input( 'Qual seu Sexo? [M/F]' ) ).upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor Inválido. Digite Novamente.')
    else:
        print('Fim')
