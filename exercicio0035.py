a = float(input('Digite o tamanho do primeiro segmento de reta: '))
b = float(input('Digite o tamanho do segundo segmento de reta: '))
c = float(input('Digite o tamanho do terceiro segmento de reta: '))
if a < (b + c) and b < (c + a) and c < (b + a):
    print('As retas a,b e c podem formar um triângulo!')
else:
    print('As retas a,b e c NÃO podem formar um triângulo!')
