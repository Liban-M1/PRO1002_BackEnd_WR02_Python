# Exercise 1: File to List Converter
filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
        print(stripped_lines)
except FileNotFoundError:
    print("Error: File not found!")




# Exercise 2: Task List Manager
def add_task(task_list, task):
    task_list.append(task)
    return task_list

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
    return task_list

task_list = []
while True:
    user_input = input("Enter 'add' or 'remove' or 'done': ")
    if user_input == 'done':
        break
    elif user_input == 'add':
        task = input("Enter task: ")
        add_task(task_list, task)
    elif user_input == 'remove':
        task = input("Enter task to remove: ")
        remove_task(task_list, task)
    print(task_list)




# Exercise 3: Simple Class and Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, my name is " + self.name)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student("John", 20, "S12345")
student.greet()
print("Student ID:", student.student_id)




# Exercise 4: Math Quiz with Exception Handling
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print("What is", num1, "+", num2, "?")
try:
    user_answer = int(input())
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong! The answer is", correct_answer)
except ValueError:
    print("Invalid input!")




# Exercise 5: Directory Lister
import os

path = input("Enter directory path: ")
try:
    items = os.listdir(path)
    print("Directory contents:")
    for item in items:
        print("-", item)
except FileNotFoundError:
    print("Error: Directory not found!")




# Exercise 6: JSON Settings Handler
import json

try:
    with open('settings.json', 'r') as file:
        settings = json.load(file)
    print("Current settings:", settings)
    
    setting_to_change = input("Which setting would you like to change? ")
    new_value = input("Enter new value: ")
    
    settings[setting_to_change] = new_value
    
    with open('settings.json', 'w') as file:
        json.dump(settings, file)
    print("Settings updated!")
except FileNotFoundError:
    print("Error: settings.json not found!")
except Exception as e:
    print("Error:", str(e))




# Exercise 7: Scoped Variables Experiment
def test_function():
    local_var = "inside function"
    print("Inside function:", local_var)

global_var = "outside function"
print("Outside function:", global_var)
test_function()
print("After function call:", global_var)




# Exercise 8: Simple Calculator Module
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    try:
        result = divide(num1, num2)
    except ZeroDivisionError:
        print("Error: Division by zero!")
        result = None
else:
    print("Invalid operation!")
    result = None

if result is not None:
    print("Result:", result)




# Exercise 9: File Filtering and Writing
filename = input("Enter filename: ")
keyword = input("Enter keyword: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    matching_lines = []
    for line in lines:
        if keyword in line:
            matching_lines.append(line)
    
    with open('filtered.txt', 'w') as file:
        file.writelines(matching_lines)
    
    print("Filtered lines written to filtered.txt")
except FileNotFoundError:
    print("Error: File not found!")




# Exercise 10: Debugging Practice
user_input = input("Enter numbers separated by spaces: ")
str_numbers = user_input.split()
print("String numbers:", str_numbers)

total = 0
for s in str_numbers:
    try:
        num = int(s)
        print("Converted:", num)
        total += num
    except ValueError:
        print("Skipping invalid number:", s)

print("Total:", total)























