
# Crie um programa que:

    # Leia duas notas de um aluno

    # Calcule sua média

    # Motre uma mensagem na tela de acordo com a média atingida

'''
         - Média abaixo de 5.0:
               REPROVADO
        - Média entre 5.0 e 6.9:
               RECUPERAÇÃO
        - Média 7.0 ou superior:
               APROVADO
'''


print('\n \033[1m =======> Saiba se você Está Reprovado ou Não! <========= \033[m \n')


nota1 = float ( input( 'Digite a Primeira Nota: ' ) )
nota2 = float ( input ( 'Digite a Segunda Nota: ' ) )

media = ( nota1 + nota2 ) / 2
print( f' \n Sua Média é: \033[1;40m {media} \033[m \n ' )

if media < 5.0:

    print(' \033[1;31;40m Você foi REPROVADO! \033[m \n')

elif media > 5.0 and media < 6.9:

    print( ' \033[1;33;40m Você ficou para RECUPERAÇÃO! \033[m \n ' )

elif media >= 7.0:

    print( ' \033[1;32;40m Parabéns! Você foi APROVADO! \033[m \n')

print( ' \033[7;40m Obriado Por Usar Meu Programa! \033[m  \033[1;31;40m <3 \033[m \n')