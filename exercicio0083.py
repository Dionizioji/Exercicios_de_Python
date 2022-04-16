print('{:=^50}'.format(' Validando expressões '))
cont1 = cont2 = 0
expressão = list()
expressão.append(str(input('Digite a sua expressão: ')))
for i, v in enumerate(expressão):
    if v == '(':
        cont1 += 1
    if v == ')':
        cont2 += 1
if cont1 == cont2:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
