print('{:=^100}'.format(' Leitor de sexo '))
sexo = str(input('Qual é o seu sexo? [M\F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Qual é o seu sexo? [M\F] ')).strip().upper()[0]
print('Obrigado! Sexo {} registrado.'.format(sexo))
