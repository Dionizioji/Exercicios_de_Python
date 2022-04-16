print('{:=^50}'.format(' Lista de melhores campanhas NBA 2020 '))
times = ('Bucks', 'Lakers', 'Raptors', 'Clippers', 'Celtics', 'Nuggets', 'Rockets', 'Heat', 'Jazz', 'Thunder')
print('{:=^50}'.format(''))
print(times)
print('{:=^50}'.format(''))
print(f'Os 5 primeiros colocados foram: {(times[0:5])}')
print(f'Os 4 últimos foram: {(times[-4:])}')
print(f'Os times em ordem alfabética são:{sorted(times)}')
print(f'O Clippers está na {times.index("Clippers")+1}ª posição ')

for c in times:
    if c == 'Clippers':
        print(f'O Clippers está na posição {(times.index(c))+1}')