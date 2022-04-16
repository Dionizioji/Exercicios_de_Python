from time import sleep
print('-='*50)
print('{:^50}'.format('Olá! Nosso caixa possui somente cédulas de 50, 20, 10 e 1 real '))
print('-='*50)
aux = nota50 = nota20 = nota10 = nota1 = 0
while True:
    saída = ''
    valor = int(input('Qual valor você deseja sacar? '))
    nota50 = (valor - (valor % 50))/50
    aux = valor - (nota50*50)
    nota20 = (aux - (aux % 20))/20
    aux = valor - ((nota20*20)+(nota50*50))
    nota10 = (aux - (aux % 10))/10
    aux = valor - ((nota50*50)+(nota20*20)+(nota10*10))
    nota1 = (aux - (aux % 1))/1
    print('-=' * 50)
    print(f'''Você receberá:
    {nota50} cédulas de R$ 50,00 
    {nota20} cédulas de R$ 20,00
    {nota10} cédulas de R$ 10,00
    {nota1} cédulas de R$ 1,00''')
    print('-=' * 50)
    saída = str(input('Deseja sacar outro valor? [S/N] ')).strip().upper()
    while saída not in 'SN':
        saída = str(input('Deseja sacar outro valor? [S/N] ')).strip().upper()
    if saída == 'N':
        break
print('Saindo do sistema, aguarde!')
sleep(2)
print('-='*50)
print('Volte Sempre!!!')
print('-='*50)
