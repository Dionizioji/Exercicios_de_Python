print('{:=^100}'.format(' Tabuada v.3.0 '))
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('{:*^100}'.format(''))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('{:=^100}'.format(''))
print('{:*^100}'.format(' PROGRAMA ENCERRADO!!! VOLTE SEMPRE !!! '))
