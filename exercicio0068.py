print('{:=^100}'.format(' BEM VINDO(A) AO CADASTRO! '))
mais18 = 0
homens = 0
mais20 = 0
while True:
    print('-='*30)
    print('{:=^30}'.format(' CADASTRE UMA PESSOA '))
    print('-='*30)
    sexo = ' '
    comando = ' '
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while comando not in 'SN':
        comando = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    print('-='*30)
    if idade >= 18:
        mais18 += 1
    if sexo == 'F' and idade >= 20:
        mais20 += 1
    if sexo == 'M':
        homens += 1
    if comando == 'N':
        break
print(f'''Foram cadastrados:
{homens} TOTAL DE HOMENS
{mais18} PESSOAS MAIORES DE IDADE
{mais20} MULHERES COM 20 ANOS OU MAIS
Obrigado pela participação!''')