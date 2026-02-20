
peso = float(input("Digite seu peso aqui(Em KG): "))
altura = float(input("Digite sua altura aqui(em metros): "))

imc = peso / (altura * altura)
print(f"O seu IMC é: {imc:.2f}.")
if imc < 18.8:
        print ("Voce está abaixo do peso.")

elif 18.8 <= imc <= 24.9:
        print("Seu peso está normal.")
elif 24.91 <= imc <= 29.9:
        print("Voce está com sobre peso")
else:
        print("Voce está obeso.")


