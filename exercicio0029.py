vel = float(input('Qual foi a velocidade do veículo em km/h? '))
if vel > 80:
    print('Você excedeu o limite de velocidade em {:.2f} km/h\nVoçê foi multado em R$ {:.2f} !'.format((vel - 80), ((vel - 80) * 7)))
else:
    print('Você está dentro do limite de velocidade permitido!')
print('Tenha um bom dia, dirija com segurança!')
