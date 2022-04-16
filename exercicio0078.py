from time import sleep
print('{:=^50}'.format(' Lista, maior e menor valor! '))
lista = list()
cont = posmaior = posmenor = maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Insira o valor {c} na lista: ')))
    if c == 0:
        cont += 1
        maior = lista[0]
        menor = lista[0]
    if cont >= 1 and lista[c] > maior:
        maior = lista[c]
    if cont >= 1 and lista[c] < menor:
        menor = lista[c]
print(f'O maior valor inserido foi {maior}, nas posições: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor inserido foi {menor}, nas posições: ',end='')
for j, r in enumerate(lista):
    if lista[j] == menor:
        print(f'{j}...',end='')
print('\n3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)
print('Encerrando! Tchau!')