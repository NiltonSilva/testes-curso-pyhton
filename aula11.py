nome = 'Guanabara'
# Outra forma de fazer
print('Ola! Muito prazer em te conhecer, {}{}{}.'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoEbranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoEbranco'], nome, cores['limpa']))
print(type(cores))