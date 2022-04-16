frase=str(input('Digite uma frase nome completo: ')).strip()
print('A letra ','A','aparece {} vezes no seu nome'.format(frase.upper().count('A')))
print('A primeira letra a está na posição {}'.format(frase.upper().find('A')))
print('O último a está na posição {}'.format(frase.upper().rfind('A')))
