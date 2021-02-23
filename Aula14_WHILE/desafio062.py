
# Melhore o DESAFIO 061

# Perguntando se ele deseja mostras mais alguns termos.

# O programa encerra quando ele disse que quer mostrar 0 termos

print('\n Gerador de Progressão Aritmética \n')

primeiro_termo = int ( input ( 'Primeiro Termo: ' ) )
razao = int ( input ( 'Razão: ' ) )
termo = primeiro_termo

cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')