alturas = []

print("Digite a altura de tres pessoas em centimetros:")
for x in range(3):
    alturas.append(input(f"Altura {x + 1}: "))

alturas.sort(reverse=True)

print("\nAlturas de forma decrescente:")
for x in alturas:
    print(f"{int(x)}cm e {float(x) / 100}m")
