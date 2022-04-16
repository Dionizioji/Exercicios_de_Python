print('{:=^50}'.format(' Mini calculadora! '))
op = 0
while op != 5:
    a = float(input('Digite um valor: '))
    b = float(input('Outro valor: '))
    op = int(input(
        'Qual das operações abaixo você deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n '))
    print('{:=^50}'.format(''))
    if op == 1:
        print('A soma de {} com {} é: {}'.format(a, b, a + b))
    elif op == 2:
        print('O produto entre {} e {} é: {}'.format(a, b, a * b))
    elif op == 3:
        if a < b:
            print('O maior valor foi {} e o menor foi {}'.format(b, a))
        if b < a:
            print('O maior valor foi {} e o menor foi {}'.format(a, b))
    elif op == 4:
        print('informe os números novamente! ')
    elif op == 5:
        print('Encerrando!')
    else:
        print('Opção inválida, tente novamente!')
print('Fim!')
