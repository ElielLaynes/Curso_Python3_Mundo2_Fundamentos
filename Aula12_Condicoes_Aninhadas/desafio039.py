
# faça um programa que leia o ANO DE NASCIMENTO de um jovem

# E de acordo com a sua idade, informe:

    # Se ele ainda vai se alista so serviço militar.


            # Mostar o tempo que falta para se alistar;


    # Se é hora de ele se alistar no serviço militar.



    # Se já passou do tempo do alistamento para o serviço militar.


            # Mostar quanto tempo já passou desde a data em que ele deveria ter se alistado;


# Cabeçalho

print('\n \033[1;34;40m ========> Já está na Hora do Alistamento Militar? <======== \033[m \n')

# importando biblioteca para capturar o ano atual
import datetime

# usando a funçao importada
ano_atual = datetime.date.today().year

# pergunta o ano de nascimento do usuário
ano_nascimento = int ( input( ' \033[1;40m Qual seu ANO de Nascimento? \033[m' ) )

# calcula a idade do usuário
idade = (ano_atual - ano_nascimento)


# bloco de condicional para mostrar ao usuário se é hora ou não de se alistar
if idade == 18:

        print(''' \n \033[1;31;40m Está na Hora do Seu Alistamento Militar! \n  Vá até a junta militar mais próxima de você. \033[m \n ''')

elif idade < 18:

        faltam_idade = 18 - idade # Calcula quantos anos falta para o alistamento
        
        print(' \n \033[4m Ainda não é hora de se alistar! \033[m \n ')
        print(f' Faltam \033[1;33m {faltam_idade} ano(s) \033[m Para a Data do Seu Alistamento Militar. \n')

elif idade > 18:

        passou_idade = idade - 18 # calcula quantos anos já passou do alistamento
        
        print(' \n \033[1;91;47m Já Passou a Data do Seu Alistamento! \033[m \n')
        print(f' \033[4;29m Foi há {passou_idade} Ano(s). \033[m \n ')


print( ' \033[7;40m Obriado Por Usar Meu Programa! \033[m  \033[1;31;40m <3 \033[m \n')






