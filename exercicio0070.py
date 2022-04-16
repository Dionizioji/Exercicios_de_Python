print('{:=^50}'.format(''))
print('{:^50}'.format(' LOJA DO BARATO! '))
print('{:=^50}'.format(''))
total = 0
maisdemil = 0
nomemaisbarato = ''
preçomaisbarato = 0
cont = 0
saída = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    saída = str(input('Você deseja sair? [S/N] ')).strip().upper()[0]
    print('='*50)
    while saída not in 'SN':
        saída = str(input('Você deseja sair? [S/N] ')).strip().upper()[0]
        print('='*50)
    total += preço
    cont += 1
    if cont == 1 or preço < preçomaisbarato:
        preçomaisbarato = preço
        nomemaisbarato = produto
    if preço >= 1000:
        maisdemil += 1
    if saída == 'S':
        break
print('=*'*25)
print(f'''O produto mais barato foi o(a) {nomemaisbarato}, custando R$ {preçomaisbarato:.2f}
{maisdemil} produtos custaram mil reais ou mais
O valor total da compra foi de R$ {total:.2f}''')
print('{:=^50}'.format(' FIM!!! '))