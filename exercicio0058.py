from random import randint
print('{:=^100}'.format(' Oi, aqui é o PC, adivinhe em qual número estou pensando! Entre 0 e 10, hein!? '))
n = randint(0, 10)
tentativa = 1
x = int(input('Qual foi o valor pensado pelo computador? '))
while x != n:
    print('Hmmmm...tente outra vez!')
    x = int(input('Qual foi o valor pensado pelo computador? '))
    tentativa += 1
    if x-n == 1 or n-x == 1:
        print('Tá perto!')
print('Parabéns, enfim você acertou!\nFoi na {}ª tentativa!'.format(tentativa))

