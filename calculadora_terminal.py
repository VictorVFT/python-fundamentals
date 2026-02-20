x = float(input("Insira um numero aqui"))

y = float(input("Insira um numero aqui"))

print("Escolha uma operação")

print("1. Adição")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")

escolha = input("Digite o numero da operação desejada.")

if escolha == '1' :
   resultado = x + y
   print("Resultado da adição", resultado)
elif escolha == '2' :
    resultado = x - y
    print("Resultado da subtração:", resultado)
elif escolha == '3' :
   resultado = x / y
   print("Resultado da divisão:", resultado)
elif escolha == '4' :
   resultado = x * y
   print("Resultado da multiplicação: ", resultado)

else:
   print("Escolha inválida")

