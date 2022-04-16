a = float(input('Informe o primeiro lado do triângulo: '))
b = float(input('Informe o segundo lado do triângulo: '))
c = float(input('Informe o terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < b + a:
    print('Os lados a,b e c de medidas {:.2f},{:.2f} e {:.2f} unidades podem formar um triângulo'.format(a, b, c))
    if a != b != c and a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('O triângulo é escaleno e retângulo!')
    elif a != b != c and a != c:
        print('O triângulo é escaleno!')
    elif a == b == c:
        print('O triângulo é equilátero!')
    elif a == b and a != c or b == c and c != a:
        print('O triângulo é isósceles!')
else:
    print('Não é possível formar um triângulo com as medidas {:.2f},{:.2f} e {:.2f} apresentadas'.format(a, b, c))
