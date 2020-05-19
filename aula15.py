'''
cont = 1
while cont <= 10:
    print(cont, end='')
    print(' -> ' if cont < 10 else '\nAcabou', end='')
    cont += 1
'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}.')
print('O {} tem {} anos.'.format(nome, idade))