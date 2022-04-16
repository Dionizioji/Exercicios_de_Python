from time import sleep
from random import randint
print('{:=^50}'.format(' PEDRA, PAPEl, TESOURA '))
opção = int(input('[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nQual é a sua escolha? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
pc = randint(0, 2)
print('-='*25)
if pc == 0 and opção == 1:
    print('Computador jogou PEDRA\nVocê jogou PAPEL')
    print('{:=^50}'.format(''))
    print('Que pena! Você perdeu!')
elif pc == 0 and opção == 2:
    print('Computador jogou PEDRA\nVocê jogou TESOURA')
    print('{:=^50}'.format(''))
    print('Que pena! Você perdeu!')
elif pc == 1 and opção == 0:
    print('Computador jogou PAPEL\nVocê jogou PEDRA')
    print('{:=^50}'.format(''))
    print('Que pena! Você perdeu!')
elif pc == 1 and opção == 2:
    print('Computador jogou PAPEL\nVocê jogou TESOURA')
    print('{:=^50}'.format(''))
    print('Parabéns! Você ganhou!')
elif pc == 2 and opção == 0:
    print('Computador jogou TESOURA\nVocê jogou PEDRA')
    print('{:=^50}'.format(''))
    print('Parabéns! Você ganhou!')
elif pc == 2 and opção == 1:
    print('Computador jogou TESOURA\nVocê jogou PAPEL')
    print('{:=^50}'.format(''))
    print('Que pena! Você perdeu!')
elif pc == 0 and opção == 0:
    print('Computador jogou PEDRA\nVocê jogou PEDRA')
    print('{:=^50}'.format(''))
    print('Vocês empataram!')
elif pc == 1 and opção == 1:
    print('Computador jogou PAPEL\nVocê jogou PAPEL')
    print('{:=^50}'.format(''))
    print('Vocês empataram!')
elif pc == 2 and opção == 2:
    print('Computador jogou TESOURA\nVocê jogou TESOURA')
    print('{:=^50}'.format(''))
    print('Vocês empataram!')
