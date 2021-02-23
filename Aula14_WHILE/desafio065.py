
# Crie um programa que leia vários númeors inteiros pelo teclado

# Peguntar se o usuário quer ou não continuar

# No final da execução, mostre a 
# 
# A MÉDIA entre todos os valores
# qual foi MAIOR valor
# qual foi MENOR valor


resp = 'S'

soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int ( input ( 'Digite um Número: ' ) )
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str ( input ( 'Quer Continuar? [S?N] ' ) ).upper().strip()[0]

media = soma / quant

print(f'Você Digitou {quant} números e a Média foi: {media:.2f}')
print(f'O Maior valor foi: {maior} e o Menor foi: {menor}')