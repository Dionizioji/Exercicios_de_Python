valores = list()
for d in range(0, 7):
    valores.append(int(input('Insira um valor na lista: ')))
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')