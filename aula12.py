nome=str(input('Qual é o seu nome? '))
if nome == 'Dionizio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito comum no Brasil!')
else:
    print('Seu nome é meio...mehhh!')
print('Tenha um bom dia, {}!'.format(nome))