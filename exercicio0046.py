from time import sleep
import emoji
print('Vamos começar a contagem regressiva!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize('FELIZ ANO NOVO!!! :bomb:', use_aliases=True))

