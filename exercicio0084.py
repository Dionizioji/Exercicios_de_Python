print('{:=^50}'.format(' 1º Exercício e Lista Composta '))
cont = mleve = mpesada = 0
lista1 = list()
lista2 = list()
leves = list()
pesadas = list()
mleve = mpesado = aux = 0
while True:
    lista1.append((str(input('Digite um nome: '))))
    lista1.append((int(input('Digite a idade: '))))
    lista1.append((int(input('Digite o seu peso: '))))
    if aux == 0:
        mleve = mpesado = lista1[-1]
        aux += 1
    if lista1[-1] > mpesado:
        leves.append(lista1[-3])
        mpesado = lista1[-1]
    elif lista1[-1] < mleve:
        pesadas.append(lista1[-3])
        mleve = lista1[-1]
    lista2.append(lista1[-3:])
    cont += 1
    saída = str(input('Deseja sair? [N/S] ')).strip().upper()
    if saída == 'S':
        break
    while saída not in 'SN':
        saída = str(input('Entrada errada! Deseja sair? [N/S] ')).strip().upper()
print(lista1)
print(lista2)
print(f'Ao todo,{cont} pessoa(s) foram cadastradas! ')
print(f'{pesadas} são as pessoas acima do peso, com {mpesado} kg!')
print(f'{leves} são as pessoas abaixo do peso, com {mleve} kg!')

