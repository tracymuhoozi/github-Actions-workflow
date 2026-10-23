def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    return a/b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot take the modulus by zero")
    return a%b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            
def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
        "5": ("Modulus", modulus),
    }  
    while True:
        print("\n=== Calculator ===")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("q. Quit")
        
        choice = input("Choose an operation: ").strip().lower()
        
        if choice == "q":
            print("Goodbye!")
            break
        
        if choice not in operations:
            print("Invalid choice. Please try again.")   
            continue
        
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        
        name, func = operations[choice]  
        try:
            result = func(a, b)
            print(f"{name} result: {result}")  
            
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            
if __name__ == "__main__":
    main()                       