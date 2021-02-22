
# A Confederação nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com idade:

# ... Crie um programa que:

    # leia o ANO DE NASCIMENTO de um atleta

    # Mostre sua categoria de acordo com a idade

'''
            -> Até 9 anos: Mirim
            -> Até 14 anos: Infantil
            -> Até 19 anos: junior
            -> até 20 anos: Sênior
            -> Acima de 20 anos: Mater
'''

# cabeçalho
print(' \n \033[1;40m ====> Veja em Qual Categoria de Natação Você Se Enquadra <==== \033[m \n ')

print(''' 
            CATEGORIAS:
    - Mirim
    - Infantil
    - junior
    - Sênior
    - Master
''')

# Importando biblioteca datetime
import datetime

# Pergunta o Ano
ano_nascimento = int (input('\033[7;40m Qual é Seu Ano de Nascimento?\033[m '))

# Pega apenas o ano atual da data
ano_atual = datetime.date.today().year

# calcula a idade do usuário
idade = (ano_atual - ano_nascimento)


# Condições para mostrar a categoria de acordo com a idade
if idade <= 9:

    print( '\n Categoria: \033[1;36;40m MIRIM \033[m \n' ) # Ciano 36

elif idade > 9 and idade <= 14:

    print( '\n Catogiria: \033[1;32;40m INFANTIL \033[m \n' ) # verde 32

elif idade > 14 and idade <= 19:

    print( '\n Categoria: \033[4;29;40m JUNIOR \033[m \n' ) # branco 29

elif idade <= 20:
    print( '\n Categoria: \033[1;33;40m SÊNIOR \033[m \n' ) # amarelo 33

else:
    print( '\n Categoria: \033[4;31;40m MASTER \033[m \n' ) # vermelho 31



print( ' \033[7;40m Obriado Por Usar Meu Programa! \033[m  \033[1;31;40m <3 \033[m \n')