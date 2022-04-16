from time import sleep
print('{:=^100}'.format(' Calculadora de fatorial! '))
option = 0
while option != 2:
    fat = 1
    n = int(input('Digite o número do qual vc deseja calcular o fatorial: '))
    option = int(input('[1] Calcular o fatorial\n[2] Sair\nEscolha uma opção do menu: '))
    if option == 2:
        print('Encerrando!')
        print('{:=^100}'.format(''))
        sleep(1)
        print('3...',end='')
        sleep(1)
        print('2...',end='')
        sleep(1)
        print('1...',end='')
    elif option == 1:
        for t in range(n, 0, -1):
            fat *= t
            print(t , end=' ')
            print('x ' if t > 1 else '', end='')
        print('\n{}! é igual a {}'.format(n, fat))
        print('{:=^100}'.format(''))
    else:
        print('Entrada inválida!')
        print('{:=^100}'.format(''))
print('Bye bye!!!')
