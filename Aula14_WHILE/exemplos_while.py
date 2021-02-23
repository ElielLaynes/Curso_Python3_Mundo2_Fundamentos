'''
        >>>>   ESTRUTURA DE REPETIÇÃO E CONTROLE - WHILE    <<<<

Observação inicial: O WHILE SER PARA QUANTO EU SE E TAMBÉM NÃO SEI O LIMITE. PARA AS DUAS SITUAÇÕES. JÁ O FOR, CONSIGO USAR APENAS QUANDO SEI O LIMITE.

    A estrutura de repetição FOR é muito boa quando se tem um limite sabido. Por exemplo. Execute tal comando no intervalo de 1 até 10.

    Já a Esrutura WHILE, funciona muito bem e substitui o FOR quando não se sabe até onde o intervalo vai.
    Exemplo, o intevalo começa em 1 mas eu não sei o final dele, nesse caso usa WHILE.


While funciona com condifionais if para que possamos colocar diversas excessões de iteração


    Em portugol:

    enquanto não maça
        se tem chão
            passo
        se tem buraco
            pula
        se tem moeda
            pega
    pega


    Em Python

    while not maça:
        if tem chão:
            passo
        if tem buraco:
            pulo
        if tem moeda:
            pega
    pega

        enquanto eu não chegar no final, execute o comando.


        while not x:
            passo
        pega


        c = 1

        enquanto contador != 10:
            print(contador)
            contador += 1

    -> Exemplo em python

        c = 1

        while c != 10:
            print(c)
            c += 1
        print('acabou')

'''


# Exemplos Práticos 




# usando WHILE sabendo os Limite

contador = 1

while contador < 10:
    print(contador)
    contador += 1
print('fim')


# usando com flag ou condição de parada

n = 1

while n != 0:
    n = int(input('Digite um número: '))
print('fim')



# Condição de para com S ou N

resp = 'S'

while resp == 'S':
    num = int(input( 'Digite um valor: ') )
    resp = str(input('Quer continuar? [S/N]')).upper()
print('fim')


# Separando Número Pares e Ímpares


num = 1
par = impar = 0

while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar +=1
print(f'Você Digitou {par} pares e {impar} Ímpares')
