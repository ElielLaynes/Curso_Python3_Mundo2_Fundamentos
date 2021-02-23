# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa

    # O programa vai precisar fazer as seguintes operaçoes
    
    # Passo 1
        # Perguntar o VALOR DA CASA
        # Perguntar o SALÁRIO do comprador
        # Perguntar em QUANTOS ANOS ele quer pagar

    # Passo 2
        # Calcular o valor da prestação mensal
            # A prestação no pode ser MAIOR que 30% do salário do usuário


print()
print('======= Consulte o Valor das Parcelas do seu Finânciamento =====')
print()

valor_casa = float ( input( 'Qual o Valor total do Imóvel? R$ ' ) )
salario = float ( input( 'Qual é o Seu Salário Atual? R$ ' ) )
tempo_parcela = int ( input( 'Em quantos ANOS Você Deseja Pagar? ' ) )

ano_para_mes = tempo_parcela * 12 # Conveter ano em mês

parcela_mensal = valor_casa / ano_para_mes # calcula o valor total do imóvel pela quantidade de meses

trinta_por_cento = (salario * 30) / 100 # Calculo de 30% do salário

print()
if trinta_por_cento > parcela_mensal:
    print(f'\033[1;32;40mParabéns. Finaciamento APROVADO!\033[m\n')
    print(f'O valor da parcela para essas condiçoes é: R$ {parcela_mensal:.3f} reais por mês.\n')
    print(f'Serão necessários {ano_para_mes} meses para Quitar o Finaciamento.')
else:
    print(f'\033[1;29;41mFinancimento NEGADO! O valor da parcela Execede 30% do Seu salário Atual.\033[m\n')
    print(f'Valor da parcela: R$ {parcela_mensal:.3f} reais.\n')
    print(f'Seu Salário Atual: R$ {salario:.3f} reais.\n')
    print(f'30% do Seu Salário Atual: R$ {trinta_por_cento:.3f} reais.\n')
