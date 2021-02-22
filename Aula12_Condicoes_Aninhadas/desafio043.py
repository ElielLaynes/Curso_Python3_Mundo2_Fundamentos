
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 

# calcule seu IMC de acordo com a tabela abaixo:
    # CALCULO DO IMC: divide-se o peso do paciente pela sua altura elevada ao quadrado. Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.
'''
            (PESO / ALTURA) ** 2



        - Abaixo de 18.5: Abaixo do Peso
        - Entre 18.5 e 25: Peso normal
        - 25 até 30: Sobrepeso
        - 30 até 40: Obesidade
        - Acima de 40: Obesidade grave
'''

# Cabeçalho
print('\n =====> \033[7;40m Calcule seu IMC - Índice de Massa Corpórea \033[m <===== \n')

# Recebendo os valores e guardando nas variáveis, peso e altura.
peso = float ( input ( 'Qual é Seu o Peso? (ex.:63.7)  ' ) )
altura = float ( input ( 'Qual é a Sua Altura? (ex.:1.72)  ' ) )

# Calculo do IMC
imc = peso / altura ** 2
print( str ( f' \n \033[1;40m SEU IMC: {imc:.1f} \033[m \n ' ).replace( '.' , ',' ) ) # Saída formatada do IMC


# Bloco de condicionais if para saída pesonalizad de acordo com o valor do calculo do IMC.
if ( imc < 18.5 ):

    print( ' \033[1;31;40m -> Abaixo do Peso \033[m ' )

elif ( imc >= 18.5 ) and ( imc < 25 ):

    print( ' \033[1;32;40m -> Peso Normal \033[m ' )

elif ( imc >= 25 ) and ( imc < 30 ):

    print( ' \033[1;33;40m -> Sobrepeso \033[m ' )

elif ( imc >= 30 ) and ( imc < 40 ):

    print( ' \033[1;31;40m -> Obesidade \033[m ' )

else:

    print( ' \033[1;31;40m Obesidade Grave \033[m ' )


# Saída formatada para consultados do grau de obesidade.
print(''' 
                    \033[1;37;40m >>> VEJA A INTERPRETAÇÃO DO IMC <<< \033[m

    \033[1;29m IMC	           CLASSIFICAÇÃO	        OBESIDADE (GRAU) \033[m

   \033[4;91mMENOR QUE 18,5           MAGREZA                             0\033[m \n
   \033[4;92mENTRE 18,5 E 24,9        NORMAL                              0\033[m \n
   \033[4;93mENTRE 25,0 E 29,9        SOBREPESO                           I\033[m \n
   \033[4;91mENTRE 30,0 E 39,9        OBESIDADE                           II\033[m \n
   \033[4;91mMAIOR QUE 40,0           OBESIDADE GRAVE                     III\033[m \n
''')


print( ' \n \033[7;40m Obriado Por Usar Meu Programa! \033[m  \033[1;31;40m <3 \033[m \n')