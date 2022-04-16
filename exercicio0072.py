print('{:=^50}'.format(' Número por extenso! (0 a 10) '))
cont = ('Zero', 'Hum', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
chave = ''
while True:
    while True:
        num = int(input('Digite um número no intervalo de 0 a 10: '))
        if 0 <= num <= 10:
            break
        print('Tente outra vez. ', end='')
    print(f'O número digitado foi {cont[num]}')
    chave = str(input('Você deseja continuar? [S/N]')).strip().upper()
    if chave == 'N':
        break
    if chave not in 'SN':
        print('Resposta inválida!')
print('Programa Encerrado!')