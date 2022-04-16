dist=float(input('Qual será a distância da viagem em km? '))
if dist<=200:
    print('O valor da passagem é de R$ {:.2f}'.format(dist*0.50))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(dist*0.45))
print('Boa viagem!')
