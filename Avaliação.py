peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
IMC=peso/(altura**2)
print(IMC)
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 24.4:
    print("Peso normal")
elif IMC < 29.0:
    print("Sobrepeso")
elif IMC < 34.9:
    print("Obesidade grau 1")
elif IMC < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")