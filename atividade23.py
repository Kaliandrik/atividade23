# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.


numero = int(input("DIGITE SEU NÚMERO: "))
print(f"A tabuada de {numero} é: ")
for i in range(1, 11):
    resultado = i * numero
    print(f"{numero} x {i} é igual a: {resultado}")