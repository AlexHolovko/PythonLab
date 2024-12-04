#Завдання 1: Перевірка високосного року
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

# Тест
test_years = [2000, 1900, 2020, 2021]
expected_results = [True, False, True, False]
for i, year in enumerate(test_years):
    print(f"Year {year}: {is_leap_year(year)} (Expected: {expected_results[i]})")

#Завдання 2: Кількість днів у місяці
def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]

# Тест
print(days_in_month(2020, 2))
print(days_in_month(2021, 2))
print(days_in_month(2021, 13))

#Завдання 3: День року
def day_of_year(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= days_in_month(year, month)):
        return None
    days = sum(days_in_month(year, m) for m in range(1, month)) + day
    return days

# Тест
print(day_of_year(2020, 3, 1))
print(day_of_year(2021, 2, 29))

#Завдання 4: Перевірка простого числа
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Тест
print([n for n in range(2, 20) if is_prime(n)])

#Завдання 5: Конвертація витрати палива
def liters_100km_to_miles_gallon(liters):
    miles_per_km = 1 / 1.609344
    gallon_per_liter = 1 / 3.785411784
    return 100 * miles_per_km * gallon_per_liter / liters

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1.609344
    liter_per_gallon = 3.785411784
    return 100 / (miles * km_per_mile / liter_per_gallon)

# Тест
print(liters_100km_to_miles_gallon(3.9))
print(miles_gallon_to_liters_100km(60.31143162393162))

#Завдання 6: Чи можна утворити трикутник
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Тест
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 1, 3))

#Завдання 7: Прямокутний трикутник

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

# Тест
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 1, 1))
