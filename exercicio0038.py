n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite mais um número qualquer: '))
if n1 > n2:
    print('O número {} é maior que {}!'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que {}!'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais!')
