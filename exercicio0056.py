print('{:=^100}'.format(' Analisador total '))
n = int(input('Quantas pessoas deseja analisar? '))
maisvelho = 0
idadetotal = 0
cont20 = 0
hmaisvelho = ''
for r in range(1, n+1):
    print('{:=^50}'.format(' {}ª pessoa ').format(r))
    nome = str(input('Nome: ')).strip()
    gênero = str(input('Sexo [f/m]: ')).upper()
    idade = int(input('Idade: '))
    idadetotal += idade
    if gênero == 'F' and idade >= 20:
        cont20 += 1
    if maisvelho < idade and gênero == 'M':
        maisvelho = idade
        hmaisvelho = nome
print('{:=^50}'.format(''))
print('{} mulher(es) tem mais de 20 anos.'.format(cont20))
print('O homem mais velho se chama {} e tem {} anos'.format(hmaisvelho,maisvelho))
print('A soma das idades é igual a {}'.format(idadetotal))