n = int(input('Qual tabuada você desaja vizualizar? '))
for c in range (0,11):
    print('{} x {} = {}'.format(n, c, (n*c)))
print('{:=^50}'.format(' FIM! '))