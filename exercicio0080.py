print('{:=^50}'.format(' Cadastrando valores numéricos '))
lista = []
for a in range(0, 5):
    n = int(input('Digite um valor para ser inserido na lista: '))
    if a == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print(lista)