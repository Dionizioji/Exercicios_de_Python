peso = float(input('informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))
imc = peso/(altura**2)
print('Peso informado: {:.2f}\nAltura informada {:.2f}'.format(peso, altura))
if imc < 18.5:
    print('O IMC é de {:.2f}: ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc <= 25:
    print('O IMC é {:.2f}: PESO IDEAL!'.format(imc))
elif 25 < imc < 30:
    print('O IMC é {:.2f}: SOBREPESO!'.format(imc))
elif 30 <= imc <= 40:
    print('O IMC é {:.2f}: OBESIDADE!'.format(imc))
else:
    print('O IMC é {:.2f}: OBESIDADE MÓRBIDA!'.format(imc))
