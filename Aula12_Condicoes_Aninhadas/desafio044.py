
# Elabore um programa que calcule o valor a ser pago por um produto considerando:

    # Seu preço normal 
    
    # Condição de pagamento
'''
        - À vista dinheiro ou Cheque: 10% de desconto
        - À vista no cartão: 5% de desconto
        - Em até 2x no cartão: preço normal
        - 3x ou mais no cartão: 20% de juros
'''


# Cabeçalho
print('\n \033[7;40m ============ LOJA ELIEL ============= \033[m \n')


# Captura o valor total da compras
valor_compras = float ( input( ' \033[1m Preço Total das Compras: R$ \033[m' ) )


# Printo ilustrativo das opçoes de pagamento
print('''\n
        \033[1;40m FORMAS DE PAGAMENTO \033[m

        [ 1 ] à vista com Dinheiro  - 10% de Desconto
        [ 2 ] à vista com Cartão    - 5% de Desconto
        [ 3 ] 2x no Cartão          - Preço Normal
        [ 4 ] 3x ou mais no Cartão  - 10% de juros
''')

# Capta a opçao escolhida para o pagamento
opcao = int ( input ( '\033[1;40m Qual a Opção de Pagamento Preferida?\033[m ' ) )



# Bloco que condições para aplicar o desconto conforme a opção de pagamento escolhida
if opcao == 1:

    vc_desconto = valor_compras - (valor_compras * 10 / 100) # Desconto 10%

    print( f' \n O valor total das compras foi: R${valor_compras:.2f}. Com 10% de desconto ficou por: \033[1;32;40m R${vc_desconto:.2f} \033[m \n ' )

elif opcao == 2:

    vc_desconto = valor_compras - (valor_compras * 5 / 100) # Desconto 5%

    print( f' \n O valor total das compras foi: R${valor_compras:.2f}. Com 10% de desconto ficou por: \033[1;32;40m R${vc_desconto:.2f} \033[m \n ' )

elif opcao == 3:

    print( f' \n O valor Total das Compros foi de: \033[1;40m R${valor_compras:.2f} \033[m \n ' )

else:

    juros = valor_compras + ( ( valor_compras * 0.1 ) * 3 ) # Juros de 10%

    print( f' \n O Valor total da compra foi: R${valor_compras:.2f}. Com Juros de 10%, o total foi para: \033[1;33;40m R${juros:.2f} \033[m \n ' )
    