print('{:=^50}'.format(' Lista de Compras Tabulada '))
print('-' * 50)
print('{:^50}'.format('Lista de Preços'))
print('-' * 50)
Tupla = ('Farofa', '3.78', 'Frango', '8.00', 'Lasanha', '15.00', 'Refrigerante', '6.00', 'Abóbora', '3.20', 'Filé Mignon','47.00', 'Peixe', '18.70', 'Alho', '27.99')
for c in range(0, len(Tupla)):
    if c % 2 == 0:
        print(f'{Tupla[c]:.<20}', end='')
        print('{:.>22}'.format(''), end='')
    else:
        print('{:^2}'.format('R$'), '{:>5}'.format(Tupla[c]))
