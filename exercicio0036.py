preco = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
tempo = int(input('O valor será quitado em quantos anos? '))
prestacao = preco / (tempo*12)
if (prestacao) <= (salario * 0.30):
    print('O seu empréstimo foi aprovado!\nO valor da mensalidade será de R${:.2f}'.format(prestacao))
else:
    print(
        'O seu empréstimo foi negado\nO valor da prestação seria de R${:.2f}, excedendo em R${:.2f} o máximo permitido.'.format(prestacao, (prestacao - (salario * 0.30))))
print('Tenha um bom dia!')