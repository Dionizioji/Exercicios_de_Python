from time import sleep
print('{:=^50}'.format(' Separando listas! '))
lista = []
par = []
ímpar = []
while True:
    lista.append(int(input('Insira algum valor na lista principal: ')))
    cond = (str(input('Deseja continuar? [S/N] '))).upper().strip()
    while cond not in 'SN':
        cond = (str(input('ENTRADA INVÁLIDA. Deseja continuar? [S/N] '))).upper().strip()
    if (lista[-1]) % 2 == 0:
        par.append(lista[-1])
    elif (lista[-1]) % 2 != 0:
        ímpar.append(lista[-1])
    if cond == 'N':
        break
print('*'*50)
print('Separando')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
print(f'A lista de entrada foi: {lista}')
print(f'A lista contendo os pares foi: {sorted(par)}')
print(f'A lista contendo os ímpares foi: {sorted(ímpar)}')
print('Encerrado!')