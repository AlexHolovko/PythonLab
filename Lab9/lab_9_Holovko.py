# Приклад 1
def mysplit(input_string):
    if input_string == "":
        return []
    else:
        result = []
        word = ""
        for char in input_string:
            if char != " ":
                word += char
            else:
                if word:
                    result.append(word)
                    word = ""
        if word:
            result.append(word)
        return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(""))
print(mysplit("abc"))
# Приклад 2
def display_digit(digit):
    segments = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"],  # 9
    ]

    return segments[digit]


def print_seven_segment(number):
    digits = [int(digit) for digit in str(number)]

    for row in range(5):
        line = ""
        for digit in digits:
            line += display_digit(digit)[row] + "  "
        print(line)

number = input("Enter a number: ")
print_seven_segment(number)
#Приклад 3

def caesar_cipher(message):
    encrypted_message = ""
    for char in message:
        if 'A' <= char <= 'Z':
            encrypted_message += chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

message = input("Enter your message: ")
print(caesar_cipher(message))


#Завдання 1
def caesar_cipher():
    def get_valid_shift():
        while True:
            try:
                shift = int(input("Введіть значення зсуву (1-25): "))
                if 1 <= shift <= 25:
                    return shift
                else:
                    print("Будь ласка, введіть число в діапазоні 1-25.")
            except ValueError:
                print("Неправильний ввід. Введіть ціле число.")
    text = input("Введіть текст, який потрібно зашифрувати: ")
    shift = get_valid_shift()

    encrypted_text = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    print("Зашифрований текст:", encrypted_text)
caesar_cipher()
