#!/usr/bin/python3


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Choose an operation! ")
print("1. Add")
print("2. Subtract")
print("3. Muliply")
print("4. Divide")

choice = input("Enter your choice! (1/2/3/4) ")

num1 = float(input("Please enter your first number "))
num2 = float(input("Please enter you second number "))



if choice == '1':
    print(num1, "+", num2, "= ", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "= ", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "= ", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "= ", divide(num1, num2))

