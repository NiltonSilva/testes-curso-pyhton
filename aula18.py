'''teste = list()
teste.append('Nilton')
teste.append(33)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totalMaiorIdade = totalMenorIdade = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
# print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalMaiorIdade += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenorIdade += 1
print(f'Temos {totalMaiorIdade} maiores de idade e {totalMenorIdade} menores de idade.')
