
# Crie um programa que leia vários númeors inteiros pelo teclado

# Peguntar se o usuário quer ou não continuar

# No final da execução, mostre a 
# 
# A MÉDIA entre todos os valores
# qual foi MAIOR valor
# qual foi MENOR valor


resp = 'S'

soma = 0
quant = 0
media = 0
maior = 0 
menor = 0

while resp in 'Ss':
    num = int ( input( 'Digite um Número: ' )
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str ( input ( 'Quer Continuar? [S/N]' ) ).upper().strip()[0]
    media = soma / quant

print(f'Você digitou {quant} números e a média foi: {media}')
print(f'O Maior valor: {maior}. O menor Valor: {menor}')