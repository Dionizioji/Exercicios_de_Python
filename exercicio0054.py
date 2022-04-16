from datetime import date

ano = date.today().year
print('{:=^100}'.format(' Separando maiores de idade '))
pessoas = int(input('Qual o tamanho do grupo de pessoas? '))
maior = 0
menor = 0
for c in range(1, pessoas + 1):
    p = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    if (ano - p) >= 18:
        maior += 1
    else:
        menor += 1
print('Dentre os integrantes do grupo temos: \n{} Pessoa(as) maior(es) de idade\n{} Pessoa(as) menor(es) de idade'.format(maior, menor))
