# Escreva um programa que leia um número inteiro

# Peça para o usuário escolher qual será a base de conversão:

    # 1 - para Binário
    # 2 - para Octal
    # 3 - para Hexadecimal

# Converta para a opção escolhida

print()
print('===== PRGRAMA PARA CONVERSÃO DE NÚMEROS =====')
print()

numero = int ( input( 'Digite um Número: ' ) )

print()
print(''' Escolha uma opção de Conversão abaixo:

        1 = Binário
        2 = Octal
        3 = Hexadecimal
''')
opcao = int ( input( 'Qual sua opçao para Conversão do Número? ' ) )

if opcao == 1:
    binario = bin(numero)
    print(f'\nEsse é o número \033[31m{numero}\033[m, convertido para Binário: \033[32m{binario}\033[m\n')
elif opcao == 2:
    octal = oct(numero)
    print(f'\nEsse é o número \033[31m{numero}\033[m, convertido para Octal: \033[32m{octal}\033[m\n')
elif opcao == 3:
    hexa = hex(numero)
    print(f'\nEsse é o número \033[31m{numero}\033[m, convertido para Hexadecimal: \033[32m{hexa}\033[m\n')

