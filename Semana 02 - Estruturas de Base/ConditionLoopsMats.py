print("Digite dois numeros")
num1 = int(input())
num2 = int(input())

print("\n1. Media ponderado com pesos 2 e 3")
print("2. Quadrado da soma dos 2 numeros")
print("3. Cubo do menor numero")
option = int(input("Escolha uma opcao: "))

match option:
  case 1:
    print(f"Media ponderada: {(num1*2)+(num2*3)/2}")
  case 2:
    print(f"Quadrado da soma: {pow((num1+num2), 2)}")
  case 3:
    if num1 < num2:
      print(f"Cubo do menor numero: {pow(num1, 3)}")
    else:
      print(f"Cubo do menor numero: {pow(num2, 3)}")

