from time import sleep
print('{:=^100}'.format(' Média, menor e maior valor! '))
sair = 0
soma = 0
maior = 0
menor = 0
saída = 'N'
cont = 0
while saída != 'S':
    n = int(input('\nDigite um número qualquer: '))
    soma += n
    cont += 1
    if cont == 1:
        menor = maior = cont
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    controle = str(input('\nDeseja sair? [S]: ')).strip().upper()
    if controle == 'S':
        saída = 'S'
    elif controle == 'N':
        saída = 'N'
    else:
        print('\nEntrada inválida!')
print('\nVocê digitou {} números'.format(cont))
print('\nÁ média foi de {:.2f}\n\nO menor valor foi {}\n\nO maior valor foi {}'.format((soma/cont),menor,maior))
sleep(2)
print('\nFim!')
