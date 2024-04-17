money = float(input('Quanto dinheiro você tem na carteira? '))

taxa_dolar = 5.30
taxa_euro = 5.62
taxa_iene = 0.034

conversao_dolar = money / taxa_dolar
conversao_euro = money / taxa_euro
conversao_iene = money / taxa_iene

print('Com {} reais você consegue comprar {:.2f} dólares.'.format(money, conversao_dolar))
print('Com {} reais você pode comprar {:.2f} euros.'.format(money, conversao_euro))
print('Com {} reais você pode comprar {:.2f} ienes.'.format(money, conversao_iene))
