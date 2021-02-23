
# Crie um programa que leia:

    # Nome e preço de vários produtos

    # O programa deve perguntar se o usuário quer continuar o cadastro

# No final Mostre:

    # Qual é o TOTAL GASTO na compra

    # Quantos produtos custam MAIS de R$ 1000 reias

    # Qual é o Nome do produto MAIS BARATO

total_compra = total_mil = menor = cont = 0

barato = ' '

while True:
    nome_prod = str ( input ( 'Nome do Produto: ' ) )
    preco = float ( input ( 'Preço do Produto: R$' ) )
    cont += 1

    total_compra += preco

    if preco >= 1000:
        total_mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_prod
#    else:                      parte do código otimizada, pois os comandos aninhados são iguais
#        if preco < menor:
#            menor = preco
#            barato = nome_prod

    resp = ' '
    while resp not in 'SN':
        resp = str ( input ( 'Cadastrar Mais Produtos? [S/N]: ' ) ).strip().upper()[0]
    
    if resp == 'N':
        break

print('FIM DO PROGRAMA')
print(f'O Total da Compra foi: R${total_compra:.2f}')
print(f'O total de produtos acima de R$ 1.000 reias é: {total_mil}')
print(f'O produto mais batato custa R${menor}')