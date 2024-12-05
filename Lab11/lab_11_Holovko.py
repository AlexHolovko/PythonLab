#Приклад 1: Розширення класу Stack
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, element):
        self.__stack_list.append(element)

    def pop(self):
        if len(self.__stack_list) > 0:
            return self.__stack_list.pop()
        else:
            raise IndexError("pop from empty stack")

class StackCounter(Stack):
    def __init__(self):
        super().__init__()
        self.__pop_counter = 0

    def pop(self):
        value = super().pop()
        self.__pop_counter += 1
        return value

    def get_counter(self):
        return self.__pop_counter

# Тестування
stack = StackCounter()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.get_counter())  # 2

#Приклад 2: Реалізація класу Queue
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, element):
        self.__queue_list.insert(0, element)

    def get(self):
        if len(self.__queue_list) > 0:
            return self.__queue_list.pop()
        else:
            raise QueueError("Queue is empty")

queue = Queue()
queue.put(1)
queue.put("dog")
print(queue.get())
print(queue.get())
try:
    print(queue.get())
except QueueError as e:
    print("Queue error")

#Завдання 1: Додавання методу перевірки на порожність
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, element):
        self.__queue_list.insert(0, element)

    def get(self):
        if len(self.__queue_list) > 0:
            return self.__queue_list.pop()
        else:
            raise QueueError("Queue is empty")

    def is_empty(self):
        return len(self.__queue_list) == 0
queue = Queue()
queue.put(1)
queue.put("dog")
print(queue.get())
print(queue.get())
print(queue.is_empty())
try:
    print(queue.get())
except QueueError as e:
    print("Queue empty")
