print('{:=^50}'.format(' Trabalhando com matrizes! '))
lista = [[], [], []]
pares = 0
coluna = 0
maior = 0
for c in range(0, 9):
    if c <= 2:
        valor = int(input(f'Digite o {c+1}º valor: '))
        lista[0].append(valor)
    if 2 < c <= 5:
        valor = int(input(f'Digite o {c+1}º valor: '))
        lista[1].append(valor)
    if 5 < c <= 8:
        valor = int(input(f'Digite o {c+1}º valor: '))
        lista[2].append(valor)
    if c == 2 or c == 5 or c == 8:
        coluna += valor
    if valor % 2 == 0:
        pares += valor
    if c == 0:
        maior = valor
    elif 2 < c <= 5 and maior < valor:
        maior = valor
print(f'''Os valores da matriz foram:
{lista[0]}
{lista[1]}
{lista[2]}''')
print('-='*25)
print(f'A soma dos valores pares da matriz foi igual a {pares}')
print('-+'*25)
print(f'A soma dos valores da terceira coluna foi {coluna}')
print('+='*25)
print(f'O maior valor da segunda linha foi {maior}')
