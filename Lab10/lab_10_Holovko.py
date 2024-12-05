#Приклад 1
def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"

text = input("Enter text: ")
print(is_palindrome(text))
#Приклад 2
def are_anagrams(text1, text2):
    cleaned_text1 = text1.replace(" ", "").lower()
    cleaned_text2 = text2.replace(" ", "").lower()

    if sorted(cleaned_text1) == sorted(cleaned_text2):
        return "Anagrams"
    else:
        return "Not anagrams"

text1 = input("Enter first word: ")
text2 = input("Enter second word: ")
print(are_anagrams(text1, text2))
#Приклад 3
def life_digit(birthday):
    digits = [int(digit) for digit in birthday if digit.isdigit()]

    while len(digits) > 1:
        digits_sum = sum(digits)
        digits = [int(digit) for digit in str(digits_sum)]

    return digits[0]

birthday = input("Enter your birth date (YYYYMMDD): ")
print(life_digit(birthday))

#Завдання 1
def are_hidden_chars_in_string(word, sequence):
    index = -1
    for char in word.lower():
        index = sequence.lower().find(char, index + 1)
        if index == -1:
            return "No"
    return "Yes"

word = input("Enter the first word: ")
sequence = input("Enter the second word: ")
print(are_hidden_chars_in_string(word, sequence))
#Завдання 2
def get_integer_input():
    while True:
        try:
            user_input = input("Enter an integer: ")
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

result = get_integer_input()
print(f"You entered: {result}")

#Завдання 3

def get_number_in_range(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
        except ValueError:
            print("Error: wrong input. Please enter a valid integer.")
result = get_number_in_range("Enter a number: ", 1, 10)
print(f"You entered: {result}")
