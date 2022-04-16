print('{:=^100}'.format(' Comparador de massa! '))
pessoas = int(input('Quantas pessoas serão avaliadas? '))
maior = 0
menor = 0
for c in range(1, pessoas + 1):
    massa = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    menor = massa
    if maior < menor:
        maior = massa
    elif menor > maior:
        menor = massa
print('A maior massa foi de {}'.format(maior))
print('A menor massa foi de {}'.format(menor))
