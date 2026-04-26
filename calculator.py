print("Choose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter Operation (1/2/3/4): ")

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

if choice == '1':
	print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
	print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
	print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
	print(f"{num1} / {num2} = {num1 / num2}")
else:
	print("Invalid choice.")