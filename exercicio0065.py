from time import sleep
print('{:=^100}'.format(' INTERRUPÇÃO COM FLAG '))
cont = 0
soma = 0
while True:
    n = int(input('Digite um número (Para interromper digite 999): '))
    if n == 999:
        break
    cont += 1
    soma += n
print('Interrupção acionada!!!')
print('Encerrando em...')
sleep(1)
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)
print('{:=^100}'.format(''))
print(f'Foram digitados {cont} valores e a soma foi de {soma}!')
print('{:*^100}'.format(''))
print('Its over essa bagaça!')