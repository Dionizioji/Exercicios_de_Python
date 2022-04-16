print('{:=^50}'.format(' Preenchendo e analisando a tupla! '))
tupla = ((int(input('Digite um valor: '))),(int(input('Digite outro valor: '))),(int(input('Digite outro valor: '))),(int(input('Mais um valor, por favor: '))))
print(f'Você digitou os valores: {tupla}')
print(f'Foram {tupla.count(9)} aparições do valor 9')
if tupla.index(3) != 0:
    print(f'O valor três foi digitado primeiramente na posição {tupla.index(3)}')
print(f'Os valores pares foram: ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c,'', end='')
print(f'\nOs valores ímpares foram: ',end='')
for c in tupla:
    if c % 2 != 0:
        print(c, '', end='')


