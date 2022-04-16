from random import randint
from time import sleep

print('{:=^50}'.format(' Sorteio da Mega-Sena! '))
n = int(input('Quantos sorteios você deseja realizar? '))
while True:
    for m in range(0, n):
        for k in range(0, 6):
            lista = []
            for n in range(0, 6):
                valor = randint(0, 60)
                lista.append(valor)
            print(lista)
            saída = str(input('Deseja sair? [S/N]')).upper().strip()
    while saída not in 'SN':
        saída = str(input('Entrada inválida! Deseja sair? [S/N]'))
    if saída == 'S':
        break
