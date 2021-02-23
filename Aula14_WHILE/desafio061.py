
# Refaça O DESAFIO 051 

# Lendo o PRIMEIRO TERMO e a RAZÃO de uma PA

# Mostrando os 10 PRIMEIROS TERMOS da progressão
# Usando a estrutura while

print('\n Gerador de Progressão Aritmética \n')

primeiro_termo = int ( input ( 'Primeiro Termo: ' ) )
razao = int ( input ( 'Razão: ' ) )
termo = primeiro_termo

cont = 1

while cont <=10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')