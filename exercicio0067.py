from time import sleep
from random import randint
print('-=' * 50)
print(('{:=^100}'.format(' Vamos jogar par ou ímpar? ')))
print('-=' * 50)
parganha = 0
ímparganha = 0
ganhei = 0
perdi = 0
while True:
    jogador = int(input('Digite um valor: '))
    paridade = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    if paridade != 'PI':
        print('Opção inválida!')
    if (jogador + computador) % 2 == 0 and paridade == 'P':
        print('-=' * 30)
        print('PAR!')
        print('Parabéns, você venceu!')
        print(f'O computador jogou {computador} e você jogou {jogador}')
        print('-=' * 30)
        ganhei += 1
    elif (jogador + computador) % 2 == 0 and paridade == 'I':
        print('-=' * 30)
        print('PAR!')
        print('Que pena, você perdeu! ')
        print(f'O computador jogou {computador} e você jogou {jogador}')
        perdi += 1
        print('-=' * 30)
        break
    elif (jogador + computador) % 2 != 0 and paridade == 'P':
        print('-=' * 30)
        print('ÍMPAR!')
        print('Que pena, você perdeu! ')
        print(f'O computador jogou {computador} e você jogou {jogador}')
        print('-=' * 30)
        perdi += 1
        break
    elif (jogador + computador) % 2 != 0 and paridade == 'I':
        print('-=' * 30)
        print('ÍMPAR!')
        print('Parabéns, você venceu!')
        print(f'O computador jogou {computador} e você jogou {jogador}')
        print('-=' * 30)
        ganhei += 1
print('Encerrando em...')
sleep(1)
print('3...', end='')
sleep(1)
print('2...', end='')
sleep(1)
print('1...')
sleep(1)
print('-=*' * 100)
print(f'Placar final: Computador ({perdi}) x Você ({ganhei})')
