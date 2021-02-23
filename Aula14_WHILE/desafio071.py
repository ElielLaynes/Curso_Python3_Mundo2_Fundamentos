
# Crie um programa que simule o funcionamento de UM CAIXA ELETRÔNICO

# No início pergunte ao usuário qual será o VALOR A SER SACADO (numero inteiro)

# O programa vai informar quantas cédulas de cada valor serão entregues

# OBS: Considerar que o caixa possui cédulas de R$50, R$20, R$10 e R$2


print('\n Banco 123 \n ')

valor = int ( input ( 'Digite o Valor que Deseja Sacar. R$ ' ) )
total = valor

cedula = 50
total_cedula = 0

while True:

    if total >= cedula:
        total -= cedula
        total_cedula += 1

    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} Cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        total_cedula = 0

        if total == 0:
            break