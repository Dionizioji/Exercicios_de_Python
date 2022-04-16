n = int(input('Digite um número inteiro qualquer: '))
menu = int(input('Qual das conversões deseja fazer? \n[1] para binário\n[2] para octal\n[3] para hexadecimal\nSua opção: '))
if menu == 1:
    print('A representação do número {} em binário é: {}'.format (n,bin(n)))
elif menu == 2:
    print('A representação do número {} em octal é: {}'.format (n,oct(n)))
elif menu == 3:
    print('A representação do número {} em hexadecimal é {}'.format(n,hex(n)))
else:
    print('Entrada inválida!')
