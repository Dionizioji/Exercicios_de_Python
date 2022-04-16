q = int(input('Quantos números você deseja somar, caso sejam pares? '))
soma = 0
for c in range (0,q):
    n = int(input('Digite um número qualquer: '))
    if n%2 == 0:
        soma += n
    else:
        soma = soma
print('A soma dos números pares digitados foi:{}'.format(soma))
