n = 1
pares = 0
impares = 0
total = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        total += 1
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print('Acabou')
print('A quantidade de números digitados foi {}, sendo {} impares e {} pares.'.format(total, impares, pares))