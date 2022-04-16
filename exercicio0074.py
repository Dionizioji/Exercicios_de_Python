from random import randint
print('{:=^50}'.format(' Gerando e ordenando Tupla aleatória! '))
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(tupla)
cont = 1
for c in tupla:
    if cont == 1:
        maior = tupla[0]
        menor = tupla[0]
        cont += 1
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'A tupla ordenada é {sorted(tupla)}')
print(f'O maior elemento da tupla é: {maior}')
print(f'O menor elemento da tupla é: {menor}')
print('Usando o método max e min para a tupla:')
print(f'O maior: {max(tupla)}')
print(f'O menor: {min(tupla)}')









