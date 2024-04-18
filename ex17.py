def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
  quadrado_hipotenusa = cateto_oposto ** 2 + cateto_adjacente ** 2
  hipotenusa = quadrado_hipotenusa ** 0.5  
  return hipotenusa

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')