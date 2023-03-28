n = int(input("Que termo deseja encontrar: "))

penultimo = 0
ultimo = 1

while ultimo < n:
    proximo = penultimo + ultimo
    penultimo = ultimo
    ultimo = proximo


if ultimo == n:
    print(n, "Pertence a sequência de Fibonacci")

else:
    print(n, "Não pertence à sequência de Fibonacci.")

