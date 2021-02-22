
# Faça um programa que mostre na tela:

    # Contagem REGRESSIVA para o estouro de fogos de artifício

    # Indo de 10 até 0

    # Com pausa de 1 segundo entre eles


from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Estouro de fogos de Artifício:    KABUUUM BUUUM POW PA PA POW ')
