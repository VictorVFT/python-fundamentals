P = float(input("Insira o valor inicial"))
r = float(input("Insira a taxa de juros anual"))
n = int(input("Quantas vezes esse juros é composto ao ano ?"))
t = int(input("Por quantos anos esse dinheiro será investido ?"))

M = P * (1 + (r / n)) ** (n * t)

print(" O montante acumulado é:", M)
