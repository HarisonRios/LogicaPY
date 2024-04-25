def main():
    nome_completo = input("Digite o nome completo da pessoa: ").split()
    primeiro_nome, ultimo_nome = nome_completo[0], nome_completo[-1]
    print("Primeiro nome:", primeiro_nome)
    print("Último nome:", ultimo_nome)

if __name__ == "__main__":
    main()