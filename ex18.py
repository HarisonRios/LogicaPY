## Essa foi feito com ajuda do stackowerflow e chatgpt, pois não consigo entender quase nada


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def seno(angulo):
    angulo = angulo % 360  
    angulo_rad = angulo * (3.14159265358979323846 / 180)  
    seno = angulo_rad - ((angulo_rad**3) / fatorial(3)) + ((angulo_rad**5) / fatorial(5)) - ((angulo_rad**7) / fatorial(7)) + ((angulo_rad**9) / fatorial(9)) - ((angulo_rad**11) / fatorial(11))
    return seno

def cosseno(angulo):
    angulo = angulo % 360  
    angulo_rad = angulo * (3.14159265358979323846 / 180) 
    cosseno = 1 - ((angulo_rad**2) / fatorial(2)) + ((angulo_rad**4) / fatorial(4)) - ((angulo_rad**6) / fatorial(6)) + ((angulo_rad**8) / fatorial(8)) - ((angulo_rad**10) / fatorial(10))
    return cosseno

def tangente(angulo):
    return seno(angulo) / cosseno(angulo)


angulo = float(input("Digite o valor do ângulo em graus: "))


print(f"O seno do ângulo {angulo} graus é {seno(angulo):.2f}")
print(f"O cosseno do ângulo {angulo} graus é {cosseno(angulo):.2f}")
print(f"A tangente do ângulo {angulo} graus é {tangente(angulo):.2f}")
