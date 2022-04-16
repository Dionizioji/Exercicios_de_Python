print('{:=^100}'.format(' Detector de palíndromos! '))
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('A frase {} é um palíndromo!'.format(frase))
else:
    print('A frase {} não é um palíndromo!'.format(frase))
