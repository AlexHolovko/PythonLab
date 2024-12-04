# Завдання №1: Обчислення функції Гауса
import math

def gaussian_function(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

x = 1.0
mean = 0.0
std_dev = 1.0
result = gaussian_function(x, mean, std_dev)
print("f(x) =", result)

# Завдання №2: Яблука
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=", ")

total_apples = john + mary + adam

print("Загальна кількість яблук:", total_apples)

#Завдання №3: Конвертація миль і кілометрів
miles = 7.38
kilometers = 12.25

miles_to_km = miles * 1.61
km_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_km, 2), "kilometers")
print(kilometers, "kilometers is", round(km_to_miles, 2), "miles")

# Завдання №4: Оцінка виразу
x = float(input("Enter value for x: "))
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
# Завдання №5: Покращення коментарів
hours = 2

print("Hours:", hours)
# Завдання №6: Арифметичні операції
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Division by zero error"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
#Завдання №7: Оцінка складного виразу
x = float(input("Enter value for x: "))
y = x / (1 + x**2)**0.5
print("y =", y)

#Завдання №8: Обчислення часу завершення події
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Обчислення нових значень
total_minutes = hour * 60 + mins + dura
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

# Виведення результату
print(f"{end_hour}:{end_minute}")
