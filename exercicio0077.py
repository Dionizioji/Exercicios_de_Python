print('\n{:=^50}'.format(' Analisando vogais! '))
tupla = ('Abacate', 'Abacaxi', 'Mexirica', 'Caqui', 'Goiaba', 'Morango', 'jabuticaba', 'Carambola', 'Uva', 'Amora', 'Banana')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos as vogais: ',end='')
    for d in c:
        if d.upper() in 'AEIOU':
            print(d.upper(), end=' ')


