

# Crie um  programa que leia VÁRIOS NÚMEROS inteiros pelo teclado

# O programa só vai parar com o usuário digitar o valor 999(Condição de Parada, ou flag)

# No final mostre:

    # Quantos números foram digitados

    # Qual a soma entre eles(desconsiderando o número 999 que é a flag)

soma = cont = 0

while True:

    num = int ( input ( 'Digite um Número [Digite 999 para Sair] : ' ) )

    if num != 999:
        soma += num
        cont += 1

    if num == 999:
        break

print(f'A Soma: {soma}')
print(f'Total Número Digitados: {cont}')
print('FIM')