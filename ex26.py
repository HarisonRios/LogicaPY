def main():
    frase = input("Digite uma frase: ")

    frase = frase.lower()
    vezes_a = frase.count('a')

   
    primeira_posicao = frase.find('a')
    ultima_posicao = frase.rfind('a')
    
    print("Quantidade de vezes que 'a' aparece:", vezes_a)
    if vezes_a > 0:
        print("Posição da primeira ocorrência de 'a':", primeira_posicao)
        print("Posição da última ocorrência de 'a':", ultima_posicao)
    else:
        print("A letra 'a' não aparece na frase.")

if __name__ == "__main__":
    main()