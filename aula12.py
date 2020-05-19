nome = str(input('Qual é o seu nome? ')).strip()
# '.strip' tira os espaços do começo e do final da palavra

if nome == 'Nilton':
# '.upper' torna toda a palavra em maiúsculo
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))
