def main():
    nome = input("Digite o nome completo da pessoa: ").strip().lower()
    tem_silva = "silva" in nome
    print("Tem 'Silva' no nome:", tem_silva)

if __name__ == "__main__":
    main()
