#Teste IF
print("Teste IF")

a = 200
b = 33

if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")
	
#Loop While
print("Loop While")
i = 1
while i < 6:
	print(i)
	i+= 1
	
#Loop for
print("Loop for range (6)")
for x in range(6):
	print(x)
	
print("Loop for range(2,6)")
for x in range(2, 6):
	print(f"{x}", end="")
	
print("\nLoop for sobre lista e com break")
fruits = ["apple", "lemon", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		break
	print(x)
