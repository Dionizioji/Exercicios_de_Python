print('{:=^50}'.format(' Cadastrando valores únicos! '))
lista = list()
aux = 0
while True:
    aux = int(input('Digite uma valor para ser inserido na lista: '))
    if aux not in lista:
        lista.append(aux)
    else:
        print('Valor já adicionado anteriormente!')
    saída = str(input('Deseja sair?  [S/N] ')).upper().strip()
    while saída not in 'SN':
        print('Entrada inválida')
        saída = str(input('Deseja sair? [S/N]')).upper().strip()
    if saída == 'S':
        break
print(f'Os valores digitados ordenadamente foram: {sorted(lista)}')