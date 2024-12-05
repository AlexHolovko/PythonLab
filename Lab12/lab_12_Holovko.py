#Приклад 1: Клас Timer
class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    def next_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
        if self.__minute == 60:
            self.__minute = 0
            self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0

    def previous_second(self):
        self.__second -= 1
        if self.__second == -1:
            self.__second = 59
            self.__minute -= 1
        if self.__minute == -1:
            self.__minute = 59
            self.__hour -= 1
        if self.__hour == -1:
            self.__hour = 23

# Тестування
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)

#Приклад 2: Клас Weeker
class WeekDayError(Exception):
    pass

class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError("Invalid day name")
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        index = (self.__days.index(self.__current_day) + n) % len(self.__days)
        self.__current_day = self.__days[index]

    def subtract_days(self, n):
        index = (self.__days.index(self.__current_day) - n) % len(self.__days)
        self.__current_day = self.__days[index]

# Тестування
try:
    week = Weeker("Mon")
    print(week)
    week.add_days(3)
    print(week)
    week.subtract_days(5)
    print(week)
    invalid_week = Weeker("Funday")
except WeekDayError as e:
    print("Sorry, I can't serve your request.")

#Приклад 3: Клас Point
from math import hypot

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return hypot(self.__x - point.getx(), self.__y - point.gety())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_xy(1, 1))
print(point1.distance_from_point(point2))

#Завдання 1: Клас Triangle
class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        p1, p2, p3 = self.__points
        return (p1.distance_from_point(p2) +
                p2.distance_from_point(p3) +
                p3.distance_from_point(p1))

point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)
triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())
