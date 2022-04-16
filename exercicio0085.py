print('{:=^50}'.format(' Separação em pares e ímpares! '))
lista = [[],[]]
valores = 0
saída = ''
while True:
    valor = int(input('Insira um número na lista: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 != 0:
        lista[1].append(valor)
    saída = str(input('Deseja sair? [N/S]')).upper().strip()
    while saída not in 'SN':
        saída = str(input('Entrada inválida! Deseja sair? [N/S]')).upper().strip()
    if saída == 'S':
        break
lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')








