print('{:=^100}'.format(''))
print('{:^100}'.format(' Soma dos "n" primeiros termos de uma PA'))
print('{:=^100}'.format(''))
r = int(input('Qual é a razão da PA? '))
n = int(input('Qual o número de termos você deseja somar? '))
p = int(input('Qual é o primeiro termo da PA? '))
soma = p
acumulador = 0
for c in range(p, (p+((n-1)*r))+r, r):
    soma += r
    print(end='>>{}'.format(c))
    acumulador += soma
print('\nA soma dos {} primeiros termos da PA foi de {}'.format(n,acumulador))
print('{:=^100}'.format(' FIM! '))
