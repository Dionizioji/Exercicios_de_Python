from time import sleep
print('{:=^100}'.format(' Gerador de PA! '))
menu = 0
opção3 = 0
while menu != 2:
    menu = int(input('\n[1] Gerador de PA\n[2] Sair\n[3] Continuar PA anterior\nO que você deseja: '))
    if menu == 2:
        print('Encerrando!')
        sleep(2)
        print('{:=^100}'.format(''))
        print('Volte sempre!')
    elif menu == 1:
        opção3 = 3
        p = int(input('Qual é o primeiro termo da PA? '))
        n = int(input('Qual número de termos você deseja visualizar? '))
        r = int(input('Qual é a razão da PA? '))
        print('\n{:=^100}'.format(''))
        for c in range(p, (p+((n-1)*r)+1), r):
            print(c, ' >> ', end='')
        print('\n{:=^100}'.format(''))
    elif menu == 3 and opção3 == 3:
        enésimo = (p+((n-1)*r))
        n2 = int(input('Quantos termos mais vc deseja visualizar? '))
        print('{:=^100}'.format(''))
        while n2 != 0:
            n2 -= 1
            enésimo += r
            print(enésimo , ' >> ' , end='')
        print('\n{:=^100}'.format(''))
    else:
        print('Entrada inválida!')
