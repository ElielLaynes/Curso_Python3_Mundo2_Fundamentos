
# Faça um programa que leia:

    # O peso de cinco pessoas

    # Mostre qual foi o MAIOR PESO lido

    # Mostre qual foi o MENOR PESO lido


maior = 0
menor = 0

for p in range(1, 6):
    peso = float ( input ( f'Peso da {p} pessoa:  ' ) )

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso    
        if peso < menor:
            menor = peso
print(f'O Maior peso é: {maior}')
print(f'O menor peso é: {menor}')