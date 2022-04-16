n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('Parabéns! Você foi aprovado, a sua média foi de {:.2f} pontos'.format(media))
elif media < 5:
    print('Infelizmente você foi reprovado, tente novamente. A sua média foi de {:.2f} pontos'.format(media))
else:
    print('A sua média foi de {}, estude para a prova de recuperação!'.format(media))