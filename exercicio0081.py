print('{:=^50}'.format(' Buscando infos na lista! '))
cont = 0
lista = []
saída = 'S'
cont5 = 0
while True:
    n = int(input('Digite um valor para ser inserido na lista: '))
    lista.append(n)
    if n == 5:
        cont5 += 1
    saída = str(input('Deseja sair do preenchimento de lista? [S/N] ')).upper().strip()
    while saída not in 'SN':
        saída = str(input('Deseja sair? [S/N]')).upper().strip()
    if saída == 'S':
        break
print('*'*50)
print(lista)
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: {lista}')
print(f'O número 5 foi inserido {cont5} vez(es)!')
print(f'A lista contém {len(lista)} elementos!')
