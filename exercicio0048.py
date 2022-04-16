print('{:=^100}'.format(' Soma de ímpares múltiplos de 3 '))
tamanho = int(input('Digite o tamanho do intervalo para a soma:'))
soma = 0
for c in range (1,tamanho+1,2):
    if c%3==0:
        soma += c
    else:
        soma == soma
print('A soma de todos os ímpares múltiplos de 3 no intervalo de 0 até {} é: {}'.format(tamanho,soma))