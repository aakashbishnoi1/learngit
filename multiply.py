a = input("Enter a number: ")
b = input("Enter a number: ")

try:
    a = int(a)
    b = int(b)
except ValueError: 
    print("Please enter a number")
else:
    print(a * b)