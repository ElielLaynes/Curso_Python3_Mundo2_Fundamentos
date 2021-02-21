
nome = str ( input('Qual é o seu nome? '))
if nome == 'Eliel':
    print(f'Que nome legalll :D')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print(f'Seu nome é bem popular no Brasil, {nome}.')
elif nome in 'Ana, Julia, Amanda':
    print('Que nome da hora!')
else: # Else é opcional
    print('Seu nome é bem comum.')
print(f'Tenha um bom dia, {nome}!')



