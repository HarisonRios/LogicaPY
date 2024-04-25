def main():
    numero = int(input("Digite um número de 0 a 9999: "))

    if numero < 0 or numero > 9999:
        print("Número inválido. Por favor, digite um número de 0 a 9999.")
        return
    
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    print("Unidade:", unidade)
    print("Dezena:", dezena)
    print("Centena:", centena)
    print("Milhar:", milhar)

if __name__ == "__main__":
    main()
