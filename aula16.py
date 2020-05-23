'''
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comí que fiquei triste.')
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
print(c)
print(c.count(0))
print(c.index(8))
d = b + a
print(d)
print(d.index(5, 1))
'''

pessoa = ('Gustavo', 39, 'Masculino', 99)
print(pessoa)