entrada = input("Digite qualquer coisa: ")

print("Tipo Primitivo: {}.".format(type(entrada)))

print("É Numérico? {}".format(entrada.isnumeric()))
print("É Alfa Numérico? {}".format(entrada.isalpha()))
print("É Decimal? {}".format(entrada.isdecimal()))
print("É Minusculo? {}".format(entrada.isslower()))
print("Tem espaço? {}".format(entrada.isspace()))
print("É Maiscula? {}".format(entrada.isupper()))