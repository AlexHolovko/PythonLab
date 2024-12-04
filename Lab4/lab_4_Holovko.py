# Завдання №1:
n = int(input("Enter an integer: "))
print(n >= 100)

# Завдання №2:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if a > b:
    print("The greater number is:", a)
else:
    print("The greater number is:", b)


#Завдання №3:
user_input = input("Enter the plant name: ")
if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {user_input}!")

# Завдання №4:
income = float(input("Enter your income: "))
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = max(0, round(tax, 2))
print(f"The tax is: {tax} thalers")

# Завдання №5:
year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")

# Завдання №6:
secret_number = 777

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha-ha! You're stuck in my loop!")

#Завдання №7:
import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

#Завдання №8:
while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

# Завдання №9:
user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
# Завдання №10
user_word = input("Enter a word: ").upper()
word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)

# Завдання №11
def pyramid_height(blocks):
    height = 0
    current_layer = 1

    while blocks >= current_layer:
        blocks -= current_layer
        height += 1
        current_layer += 1

    return height


# Тестові дані
test_cases = [6, 20, 1000, 2]

for blocks in test_cases:
    print(f"Blocks: {blocks}, The height of the pyramid: {pyramid_height(blocks)}")

# Завдання №12
def collatz_sequence(c0):
    if c0 <= 0:
        print("Введіть натуральне число більше 0.")
        return

    steps = 0
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    print(c0)  # Друкуємо 1
    print(f"steps = {steps}")


# Тестові дані
collatz_sequence(15)
collatz_sequence(16)
collatz_sequence(1023)
