km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))



dias_alugados = int(input("Digite a quantidade de dias pelo qual o carro foi alugado: "))
custo_total = (km_percorridos * 0.20) + (dias_alugados * 90)
print("O valor total a ser pago é R$", custo_total)
