from datetime import date
atual = date.today().year
n = int(input('Em que ano vc nasceu? '))
idade = atual - n
if idade <= 9:
    print('Vc tem {} anos. A sua categoria é MIRIM!'.format(idade))
elif 9 < idade <= 14:
    print('Vc tem {} anos. A sua categoria INFANTIL!'.format(idade))
elif 14 < idade <= 19:
    print('Vc tem {} anos. A sua categoria é JÚNIOR!'.format(idade))
elif 19 < idade <= 25:
    print('Vc tem {} anos. A sua categoria é SÊNIOR!'.format(idade))
else:
    print('Vc tem {} anos. A sua categoria é MASTER!'.format(idade))
