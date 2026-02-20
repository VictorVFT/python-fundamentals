numero = int(input("Digite um numero para calcular fatorial: "))

resultado = 1
for i in range(1, numero + 1):
      resultado *= i

print("O Fatorial  de", numero, "é", resultado)
