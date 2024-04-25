def main():
    cidade = input("Digite o nome da cidade: ").strip().lower()
    print("Começa com 'Santo':", cidade[:5] == "santo")

if __name__ == "__main__":
    main()
