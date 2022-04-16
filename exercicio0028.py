from random import randint
print('-=-'*30)
print('Olá tente adivinhar o número inteiro entre 0 e 5 que estou mentalizando agora!')
print('-=-'*30)
num = int(input('digite um número inteiro entre 0 e 5: '))
num2 = randint(0,5)
print(num2)
if num == num2:
    print('Parabéns você acertou, foi o número {}'.format(num2))
else:
    print('Você errou! Eu pensei no número {}'.format(num2))