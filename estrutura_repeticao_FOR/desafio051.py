
# Desenvolva um programa que 

    # Leia o primeiro termo e a razão de uma Progressão Aritmética (PA)

    # Mostre os 10 primeiros termos da progressão

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

decimo_termo = pt + (10 + 1) * r # conceito matemático para saber o enésimo termo de uma PA

for c in range(pt, decimo_termo + r, r):
    print(c)