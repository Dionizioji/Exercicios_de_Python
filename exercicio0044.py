valor = float(input('Qual o valor da compra: R$ '))
forma = int(input('Qual será a forma de pagamento?\n[1] à vista no dinheiro: 10% de desconto\n[2] à vista no cartão: '
                  '5% de desconto\n[3] em até 2x no cartão: preço formal\n[4] 3x ou mais no cartão: 20% de juros\n '))
if forma == 1:
    print('Você terá 10% de desconto. O valor final da compra será: R$ {:.2f}'.format(valor-(valor*0.10)))
elif forma == 2:
    print('Você terá 5% de desconto. O valor final da compra será: R$ {:.2f}'.format(valor-(valor*0.05)))
elif forma == 3:
    print('O seu pagamento será feito em duas parcelas de R$ {:.2f} '.format(valor/2))
elif forma == 4:
    p = int(input('Digite o número de parcelas desejadas: '))
    print('O valor total será de R$ {:.2f}.\nDividido em {} parcelas de R$ {:.2f} cada.'.format((valor + valor*0.20), p, (valor + valor * 0.20)/p))
else:
    print('Forma de pagamento inválida!')
