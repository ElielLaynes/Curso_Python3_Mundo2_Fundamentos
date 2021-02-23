
# Crie um programa que leia DOIS VALORES

# Mostre um MENU na tela:
'''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
'''

# O programa deverá realizar a operação solicitada em cada caso.




from time import sleep

print('\n \033[1;40m ========>>> Programa para Realizar Operaçoes Básicas <<<========  \033[m  \n')


num1 = int ( input ( ' \033[4mPrimeiro Valor:\033[m ' ) ) 
num2 = int ( input ( ' \033[4mSegundo Valor: \033[m ' ) )

opcao = 0

while ( opcao != 5 ):

    print(''' 
    \033[1;40m QUAL OPERAÇÃO VOCÊ DESEJA REALIZAR: \033[m

            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
    ''')

    opcao = int ( input ( '\033[1;40m Digite o Número da Operação Desejada: \033[m ' ) )

    if ( opcao == 1 ) :

        soma = ( num1 + num2 )
        print( f' \n A Soma entre {num1} e {num2} é: \033[1;32m {soma} \033[m ' )

    elif ( opcao == 2 ) :

        mult = ( num1 * num2 )

        print( f' \n A Multiplicação entre {num1} e {num2} é: \033[1;32m {mult} \033[m ' )

    elif ( opcao == 3 ) :

        maior = ''

        if ( num1 > num2 ) :

            maior = num1

        else:

            maior = num2

        print( f' \n O Maior número entre {num1} e {num2} é: \033[1;32m {maior} \033[m ' )
    
    elif ( opcao == 4 ) :

        print( ' \n \033[1;32;40m Informe Novos Números: \033[m \n ' )

        num1 = int ( input ( ' \033[4mPrimeiro Valor: \033[m ' ) ) 
        num2 = int ( input ( ' \033[4mSegundo Valor valor: \033[m ' ) )

    elif ( opcao == 5 ) :

        print( ' \n \033[1m Finalizando . . . \033[m \n ' )
        sleep(2)
        print( ' \033[1;40m FIM! Obrigado Por Usar meu Programa! \033[1;31m<3 \033[m \n ' )

    else:

        print( ' \n \033[1;31;40m Opção Inválida. Tente Novamente! \033[m ' )




