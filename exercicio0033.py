num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 > num2 > num3:
    print('O número {} é o maior e o número {} é o menor!'.format(num1, num3))
if num2 > num3 > num1:
    print('O número {} é o maior e o número {} é o menor!'.format(num2, num1))
if num3 > num2 > num1:
    print('O número {} é o maior e o número {} é o menor'.format(num3, num1))
if num2 > num1> num3:
    print('O número {} é o maior e o número {} é o menor!'.format(num2, num3))
if num1 > num3 > num2:
    print('O número {} é o maior e o número {} é o menor!'.format(num1, num2))
if num3> num1 > num2:
    print('O número {} é o maior e o número {} é o menor!'.format(num3, num2))

