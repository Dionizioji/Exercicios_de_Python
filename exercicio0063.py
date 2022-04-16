print('{:=^100}'.format(' Se quiser parar digite 999! '))
n = 0
soma = 0
cont = 0
n = int(input('Digite um número qualquer: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número qualquer: '))
print('Foram digitados {} números e a soma deu {}'.format(cont,soma))