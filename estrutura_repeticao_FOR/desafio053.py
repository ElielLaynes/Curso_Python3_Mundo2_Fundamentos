
# Crie um programa que leia uma frase qualquer

# Diga se ela é um PALÍNDROMO (São frases/palavras que lidas de trás para frente tem o mesmo significado)

# desconsiderando os espaços

'''
    Exemplo:

    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA
'''


frase = str ( input( 'Digite uma frase: ' ) ).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('Não é um palindromo')

