from datetime import date
sexo = int(input('Qual é o seu sexo?\n[1] para feminino\n[2] para masculino\n '))
if sexo == 1:
    print('Não é necessário se alistar!')
atual = date.today().year
if sexo == 2:
    ano = int(input('Digite o ano em que você nasceu:  '))
    idade = atual - ano
    tempo = idade - 21
    if idade > 21:
        print('Vc perdeu o prazo de alistamento, o limite foi excedido em {} anos!'.format(tempo))
    elif idade < 21:
        print('Ainda faltam {} anos pra você se alistar!'.format(tempo*(-1)))
    else:
        print('Você deve se alistar ainda este ano!')

