from math import sqrt
CO = float(input("Digite o comprimento do cateto oposto: "))
CA = float(input("Digite o comprimento do cateto adjascente "))
hip = sqrt(((CO)**2)+((CA)**2))
print("O valor da hipotenusa é de: {:.2f}".format(hip))



