
# faça um programa que 

# Jogue par ou Impar com o computador

# O jogo será INTERROMPIDO quando o JOGADOR PERDER

# Mostrando o total de vitórios consecutivas que ele conquistou no final do jogo

from random import randint

print(' ========>>>  Jogue PAR ou ÍMPAR com o Computador <<<========' )

vit = 0

while True:
    jogador = int ( input ( '\nDigite um Número: ' ) )
    computador = randint(0, 10)
    total = computador + jogador
    
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str ( input ( 'Par ou Ímpar? [P/I]: ' ) ).strip().upper()[0] # strip() tira todos os espaços antes e depois. upper() joga tudo pra caixa alta e índice [0] para pega apenas a primeira letra
    print(f'Você Jogou: {jogador} e o Computador: {computador}. Total de {total} ', end='')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if par_impar == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vit += 1
        else:
            print('Você Perdeu!')
            break

    elif par_impar == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            vit += 1
        else:
            print('Você Perdeu!')
            break
    print('Jogue Novamente...')
print(f'Fim de Jogo! Você venceu {vit} Vezes.')
    




