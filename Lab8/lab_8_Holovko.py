# Завдання 1

import module

def main():
    """Основна функція."""
    name = input("Enter your name: ")
    print(module.greeting(name))

    # Використання функції додавання чисел
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum of {a} and {b} is: {module.add_numbers(a, b)}")

if __name__ == "__main__":
    main()
# Завдання 2

from extra.math_tools import multiply, divide
from extra.string_tools import reverse_string, capitalize_string

def main():
    """Основна функція."""
    # Демонстрація математичних функцій
    print("Math tools demo:")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")

    # Демонстрація роботи з рядками
    print("\nString tools demo:")
    print(f"Reverse of 'hello' is: {reverse_string('hello')}")
    print(f"Capitalized 'world' is: {capitalize_string('world')}")

if __name__ == "__main__":
    main()

