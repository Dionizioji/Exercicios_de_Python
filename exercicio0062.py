print('{:=^100}'.format(' SEQUÊNCIA FIBONACCI '))
n = int(input('Quantos termos da sequência Fibonacci deseja visualizar? '))
t1 = 0
t2 = 1
print('{} >> {} >> '.format(t1, t2), end='')
cont = 3
while cont <= n:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' {}>> '.format(t3), end='')
print('\n')
print('='*100)
print('\nFIM!')
