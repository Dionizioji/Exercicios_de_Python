sal = float(input('Qual é o seu salário em R$? '))
if sal > 1200:
    print('O seu aumento será de 10%, seu salário reajustado é de: R$ {:.2f}'.format(sal+(sal*0.10)))
else:
    print('O seu aumento será de 15%, seu salário reajustado é de: R${:.2f}'.format(sal+(sal*0.15)))
