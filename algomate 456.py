import math
from operator import index
def fibonacci(num):
    if num < 0:
        raise ValueError("Index cannot be negative.")

    a, b = 0, 1

    for _ in range(num):
        a, b = b, a + b

    return a        


def is_prime(num):
    if num < 2:
        return False

    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False

    return True


def prime_factors(num):
    if num <= 1:
        raise ValueError("Enter a number greater than 1.")

    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1

    return factors


def remove_duplicates(values):
    return list(dict.fromkeys(values))


def read_list():
    text = input("Enter numbers separated by commas: ")
    return [int(value.strip()) for value in text.split(",")]


def number_menu():
    while True:
        print("""
Number Tools
1. GCD and LCM
2. Prime check
3. Prime factorization
4. Fibonacci
5. Factorial
6. Square root
7. Power
0. Back
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                a = int(input("First number: "))
                b = int(input("Second number: "))

                print("GCD:", math.gcd(a, b))
                print("LCM:", math.lcm(a, b))

            elif choice == "2":
                a = int(input("Number: "))
                print("Prime:", is_prime(a))

            elif choice == "3":
                n = int(input("Number: "))
                print("Factors:", prime_factors(n))

            elif choice == "4":
                a = int(input("Fibonacci index: "))

                print("Value:", fibonacci(a))
                print("Sequence: ",[fibonacci(index) for index in range(a + 1)])


            elif choice == "5":
                a = int(input("Number: "))

                if a < 0:
                    raise ValueError("Factorial is not available for negative numbers.")
                        
                print("Factorial:", math.factorial(a))    

            elif choice == "6":
                a = float(input("Number: "))

                if a < 0:
                    raise ValueError("Square root is not available for negative numbers.")
            
                print("Square root:", math.sqrt(a))

            elif choice == "7":
                base = int(input("Base: "))
                exponent = int(input("Exponent: "))

                if exponent < 0:
                    raise ValueError("Exponent cannot be negative.")
                        
                print("Result:", base ** exponent)

            elif choice == "0":
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)


def list_menu():
    while True:
        print("""
List Tools
1. Reverse list
2. Remove duplicates
3. Find maximum
4. Count occurrences
5. Find kth smallest
6. Sort list
0. Back
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                values = read_list()
                print("Reversed:", values[::-1])

            elif choice == "2":
                values = read_list()
                print("Without duplicates:", remove_duplicates(values))

            elif choice == "3":
                values = read_list()

                if not values:
                    raise ValueError("The list cannot be empty.")

                print("Maximum:", max(values))

            elif choice == "4":
                values = read_list()
                target = int(input("Value to count: "))

                print("Occurrences:", values.count(target))

            elif choice == "5":
                values = remove_duplicates(read_list())
                position = int(input("Enter k: "))

                if position < 1 or position > len(values):
                    raise ValueError("k is outside the valid range.")
            
                values.sort()

                print(f"{position}th smallest value:",
                      values[position - 1])
                    
            elif choice == "6":
                values = read_list()
                values.sort()

                print("Sorted list:", values)

            elif choice == "0":
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)


def main():
    while True:
        print("""
AlgoMate
1. Number tools
2. List tools
0. Exit
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                number_menu()

            elif choice == "2":
                list_menu()

            elif choice == "0":
                print("Goodbye,hav a great day!")
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()