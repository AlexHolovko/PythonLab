#Завдання 1: Числа з кортежу, менші за n
numbers = (10, 20, 5, 3, 15, 8)
n = int(input("Enter a number: "))

result = [x for x in numbers if x < n]

print(f"Numbers less than {n}: {result}")

#Завдання 2: З'єднання рядків у кортежі
strings = ("apple", "banana", "cherry")

result = ", ".join(strings)

print(f"Joined string: {result}")

#Завдання 3: Словник про книги
library = {
    "1984": {"author": "George Orwell", "year": 1949, "pages": 328},
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960, "pages": 281},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925, "pages": 180}
}

book_name = input("Enter book name: ")

if book_name in library:
    info = library[book_name]
    print(f"Book: {book_name}")
    print(f"Author: {info['author']}")
    print(f"Year: {info['year']}")
    print(f"Pages: {info['pages']}")
else:
    print("Book not found.")

#Завдання 4: Словник зі студентами
students = {
    "Doe": ("John", "Math, History, Biology"),
    "Smith": ("Jane", "Physics, Chemistry, English")
}

last_name = input("Enter last name: ")

if last_name in students:
    info = students[last_name]
    print(f"Student: {info[0]} {last_name}")
    print(f"Subjects: {info[1]}")
else:
    print("Student not found.")

#Завдання 5: Телефонна книга
phonebook = {
    "John Doe": ["123-456-789", "987-654-321"],
    "Jane Smith": ["555-555-555"]
}

def add_phone(contact, number):
    if contact in phonebook:
        phonebook[contact].append(number)
    else:
        phonebook[contact] = [number]

add_phone("John Doe", "111-222-333")
add_phone("New Contact", "999-888-777")

for contact, numbers in phonebook.items():
    print(f"{contact}: {', '.join(numbers)}")
