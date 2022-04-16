print('{:=^50}'.format(' Verificador de números primos '))
print('{:=^50}'.format(''))
n = int(input('Digite um número inteiro qualquer: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m',end='')
        print('{} '.format(c),end='')
        cont += 1
    else:
        print('\033[m',end='')
        print('{} '.format(c),end='')
        cont == cont
if cont <= 2:
    print('\nO número {} é primo!'.format(n),end='')
else:
    print('\nO número {} NÃO é primo!'.format(n),end='')

