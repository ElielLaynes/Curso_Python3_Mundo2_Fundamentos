
# Escreva um programa que leia dois números inteiros

# Compare-os e escreva na tela uma mensagem:

    # O PRIMEIRO valor é MAIOR

    # O SEGUNDO valor é MAIOR

    # NÃO EXISTE valor MAIOR, os dois são IGUAIS.


print()
print('===== PROGRAMA COMPARADO DE NÚMEROS =====')
print()

n1 = int ( input( 'Digite um Número: ' ) )
n2 = int ( input ( 'Digite outro Número: ' ) )

if n1 > n2:
    print(' \n \033[1;40m O PRIMEIRO número é MAIOR que o SEGUNDO. \033[m \n ')
    print(f' \033[32m {n1} \033[m  >  \033[31m {n2} \033[m \n ')
elif n1 < n2:
    print(' \n \033[1;40m O SEGUNDO número é MAIOR que o PRIMEIRO. \033[m \n ')
    print(f' \033[32m {n2} \033[m  >  \033[31m {n1} \033[m  \n ')
elif n1 == n2:
    print(f' \n \033[1;40m Os DOIS valores são IGUAIS. \033[m \n ')
    print(f' \n \033[32m {n1} \033[m  =  \033[32m {n2} \033[m \n ')

print(' \033[1;40m Obrigado por Usar meu Programa! \033[m  \033[1;31;107m <3 \033[m \n')