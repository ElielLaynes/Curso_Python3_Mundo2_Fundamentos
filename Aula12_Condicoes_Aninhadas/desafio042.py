
# Refaça o DESAFIO 035 dos triângulos, acrescetando o recurso de mostrar que tipo de triângulo será formado:

    # - Equilátero: todos os lados iguais

    # - Isósceles: dois lados iguais

    # - Escaleno: todos os lados diferentes



print ( '\n \033[1;40m =====> Essas Retas Podem Formar um Triângulo? <===== \033[m \n' )


reta1  =  float ( input ( 'Primeira Reta:' ))
reta2  =  float ( input ( 'Segunda Reta:' ))
reta3  =  float ( input ( 'Terceita Reta:' ))

if ( reta1  <  reta2  +  reta3 ) and ( reta2  <  reta1  +  reta3 ) and ( reta3  <  reta1  +  reta2 ):
    print ( f'As retas { reta1 } , { reta2 } , { reta3 } , PODEM formar um triângulo. ', end='' )
    if reta1 == reta2 == reta3:
        print('Equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print ( f'As retas { reta1 } , { reta2 } , { reta3 } , NÃO PODEM formar um triângulo. ' )

