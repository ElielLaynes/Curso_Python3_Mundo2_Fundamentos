
# Desenvolva um programa que leia 

    # Sei números inteiros 

    # Mostre a soma apenas daqueles que forem pares


soma = 0

for n in range(1, 7):
    num = int ( input ( 'Digite um número inteiro, 6 vezes: ' ) )
    if num % 2 == 0:
        soma += num
print(soma)