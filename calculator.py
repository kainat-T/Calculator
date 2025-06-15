def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def show_menu():
    print("\nSimple Calculator")
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    show_menu()
    choice = int(input("\nEnter your choice:"))

    if choice == 5:
        print("Goodbye! See you later.")
        break
    
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Try again!")
        continue

    x = float(input("\nnum1:"))
    y = float(input("num2:"))

    if choice == 1:
        print(f"Result:{add(x, y)}")
    elif choice == 2:
        print(f"Result:{subtract(x, y)}")
    elif choice == 3:
        print(f"Result:{multiply(x, y)}")
    elif choice == 4:
        print(f"Result:{divide(x, y)}")
    