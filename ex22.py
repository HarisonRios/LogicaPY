def main():
    nome_completo = input("Digite o nome completo da pessoa: ")

    nome_maiusculo = nome_completo.upper()
    print("Nome em maiúsculas:", nome_maiusculo)

    nome_minusculo = nome_completo.lower()
    print("Nome em minúsculas:", nome_minusculo)

    total_letras = len(nome_completo.replace(" ", ""))
    print("Número total de letras:", total_letras)

    primeiro_nome = nome_completo.split()[0]
    letras_primeiro_nome = len(primeiro_nome)
    print("Número de letras no primeiro nome:", letras_primeiro_nome)

if __name__ == "__main__":
    main()
