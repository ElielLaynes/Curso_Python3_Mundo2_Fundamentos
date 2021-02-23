
# faça um programa que:

# Mostre a TABUADA DE VÁRIOS NÚMEROS, uma de cada vez Para cada valor digitado pelo usuáiiro

# O programa será interrompido quando o número solicitado for NEGATIVO


while True:
    n = int ( input( 'A Tabuada de qual valor você quer ver? ' ))
    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}' )
        
print('Programa Encerrado')
