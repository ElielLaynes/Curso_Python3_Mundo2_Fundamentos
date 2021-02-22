
# Refaça o DESAFIO 009

    # Mostrando a tabuada de um número que o úsuário escolher
    # utilizando laço for



'''
num  =  int ( input ( 'Digite um Número:' ))
print ( '='  *  30 )
print ( 'A Tabuada de {} é:' . format ( num ))
print ( '='  *  30 )
print ( '{} x 0 = {: ^ 5}' . format ( num , num  *  0 ))
print ( '{} x 1 = {: ^ 5}' . format ( num , num  *  1 ))
print ( '{} x 2 = {: ^ 5}' . format ( num , num  *  2 ))
print ( '{} x 3 = {: ^ 5}' . format ( num , num  *  3 ))
print ( '{} x 4 = {: ^ 5}' . format ( num , num  *  4 ))
print ( '{} x 5 = {: ^ 5}' . format ( num , num  *  5 ))
print ( '{} x 6 = {: ^ 5}' . format ( num , num  *  6 ))
print ( '{} x 7 = {: ^ 5}' . format ( num , num  *  7 ))
print ( '{} x 8 = {: ^ 5}' . format ( num , num  *  8 ))
print ( '{} x 9 = {: ^ 5}' . format ( num , num  *  9 ))
print ( '{} x 10 = {: ^ 5}' . format ( num , num  *  10 ))'''


numero = int ( input ( 'Digite um Número para ver A Tabuada: ' ) )

for n in range(1, 11):
    print ( f'{numero} x {n:2} = {numero * n}')