import math

def calculate_roots(a, b, c):
    if a == 0:
        print("Invalid coefficients (a cannot be zero).")
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are: {root1:.2f} and {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The repeated root is: {root:.2f}")
    else:
        print("No real roots.")

def main():
    print("Select the equation type:")
    print("1. Case 1: a = 1, b = 0, c = -4")
    print("2. Case 2: a = 1, b = -4, c = 4")
    print("3. Case 3: a = 0, b = 1, c = -2 (Invalid quadratic)")
    print("4. Case 4: Custom coefficients")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    if choice == 1:
        a, b, c = 1, 0, -4
        print(f"\nCase 1 selected: a={a}, b={b}, c={c}")
    elif choice == 2:
        a, b, c = 1, -4, 4
        print(f"\nCase 2 selected: a={a}, b={b}, c={c}")
    elif choice == 3:
        a, b, c = 0, 1, -2
        print(f"\nCase 3 selected: a={a}, b={b}, c={c}")
    elif choice == 4:
        try:
            user_input = input("\nEnter custom coefficients a, b, c (space-separated): ")
            a, b, c = map(float, user_input.split())
        except ValueError:
            print("Invalid input. Please enter three numeric values.")
            return
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        return

    calculate_roots(a, b, c)

if __name__ == "__main__":
    main()