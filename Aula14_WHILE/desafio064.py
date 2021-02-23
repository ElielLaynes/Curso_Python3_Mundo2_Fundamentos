# Crie um programa que 

# Leia VÁRIOS NÚMEROS inteiros pelo teclado

# o programa só vai PARAR quanto o usuário digitar o valor 999(condição de parada)

# Mostre quantos números foram digitados

# Qual foi a soma dos números, deconsiderando o 999(condição de parada)




condicao = num_tot = soma = 0

while condicao != 999:
    num = int ( input( 'Digite um Número - [utilize 999 para Sair]: ' ))
    condicao = num

    if num != 999:
        num_tot += 1
        soma += num

print(f'\n Você Digitou {num_tot} números e a soma entre eles foi: {soma} \n')

