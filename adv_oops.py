'''Write a decorator logger that prints "Function is being called" before
the function runs. Use it to decorate a function say_hello() that prints
"Hello!"
def my_deco(func):
    def wrapper():
        print("Function is being called")
        func()
        
    return wrapper
    
@my_deco
def say_hello():
    print("Hello!")

say_hello()'''
'''Write a decorator timer that calculates how long a function takes to execute.
Test it with a function that sums numbers from 1 to 1,000,000.
import time
def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("time taken", end - start, "seconds")

        return result
    return wrapper
@timer
def sum_val():
    sum1 = 0
    for a in range (1000001):
        sum1 += a
    return sum1

print(sum_val())'''
'''Create a class Employee with a private attribute _salary .
Use @property to define a getter for salary .
Use @salary.setter to prevent setting negative values (print a warning
instead).
Create an object and test by setting positive and negative salaries.'''
'''class Employee:
    def __init__(self, salary):
        self._salary = salary
    def get_salary(self):
        return self._salary
    def set_salary(self, new_salary):
        self._salary = new_salary
e = Employee(25000)
print(e.get_salary())
print(e.set_salary(40000))
print(e.get_salary())
class Employee:
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        if (salary < 0) :
            print("salary cant be negative")
        else :
            self._salary = salary
e = Employee(25000)
print(e.salary)
e.salary = -5
print(e.salary)'''
'''Create a class MathUtils with:
A @staticmethod called add(a, b) that returns a + b .
A @classmethod called description(cls) that prints "This is a
utility class for math operations."
Call both methods without creating an object.

class MathUtils:
    species = "Math Utils"
    @staticmethod
    def add(a,b):
        return a + b

    @classmethod
    def description(cls):
        cls.species = "This is a utility class for math operations."

print(MathUtils.add(3,4))
MathUtils.description()
print(MathUtils.species)'''
'''Create a class Book with attributes title and author .
Implement __str__() so that printing the object displays "Title by
Author" .
Implement __len__() so that len(book) returns the length of the title.
Create two Book objects and test these methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return (f"{self.title} by {self.author}")
    def __len__(self):
        _len = len(self.title)
        return _len
b1 = Book("ayu", "ayush")
b2 = Book("vayu", "ayush")
#b1.__str__()
#b2.__str__()
print(b1)
print(len(b1))'''
'''Write a program that asks the user to enter a number and handles:
ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero
try :
    num = int(input("enter a number"))
    div = 10/num
except ZeroDivisionError:
    print("division by zero not possible")
except ValueError:
    print("enter a valid input")
try :
    num = int(input("enter a number"))
    div = 10/num
except (ZeroDivisionError, ValueError) as e:
    print(f"an error occcured: {e}")'''
'''Create a custom exception NegativeNumberError and raise it when the user
enters a negative number
class NegativeNumberError(Exception):
    def __init__(self, message = "Enter a positive number"):
        self.message = message
        super().__init__(self.message)

def number(num):
    if num < 0:
        raise NegativeNumberError()
    return num
try : 
    number(-5)
except NegativeNumberError as e:
    print(e) '''
'''Use map() to convert [1, 2, 3, 4, 5] into their cubes.

l1 = [1, 2, 3, 4, 5]
l_cube = list(map(lambda x: x**3, l1))
print(l_cube)'''
'''Use filter() to get only even numbers from [10, 11, 12, 13, 14]
l1 = [10, 11, 12, 13, 14]
l_even = list(filter(lambda x : x%2 == 0, l1))
print(l_even)
'''
'''Use reduce() from functools to find the product of all elements in [1, 2,
3, 4] .
from functools import reduce
l1 = [1, 2, 3, 4]
sum_reduced = reduce(lambda x, y : x+y, l1)
print(sum_reduced)'''
'''Use the walrus operator to read input until the user enters "quit" . Print each
input as it is entered.
 
while (num := input("enter a number or 'quit' to exit")) != "quit":
    print(num)'''
'''Use the walrus operator in a list comprehension to store lengths of words
from ["python", "rocks", "ai"] in a list while filtering out words shorter
than 4 characters.

len_ = ["python", "rocks", "ai"]
len_word =[l for x in len_ if (l:= len(x)) > 4]
print(len_word)'''
'''Write a function sum_all(*args) that accepts any number of integers and
returns their sum.
from functools import reduce
def sum_all(*args):
    sum_args = reduce(lambda x, y: x+y, args)
    return sum_args

print(sum_all(1,2))
def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(sum_all(1 , 2, 3))'''
'''Write a function print_details(**kwargs) that prints key-value pairs passed
as arguments, for example:
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="Alice", age=25, city="Delhi")'''
'''Combine a decorator with *args and **kwargs support so it can wrap any
function regardless of its parameters.
def my_deco(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print(result)
        print("after")
        return result
    return wrapper
@my_deco
def sum1(*args, **kwargs):
    sum_ = 0
    for arg in args:
        sum_ += arg
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            sum_ += value
    return sum_
    

sum1(4,5,67,age = 20,name = "rohit")'''
'''Implement __add__ in a Vector class so that adding two Vector objects
returns a new Vector with summed components
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(
            self.x + other.x, 
            self.y + other.y
        )
    def __str__(self):
        return f"({self.x},{self.y})"
    
v1 = Vector(4,3)
v2 = Vector(5,6)
v3 = v1+v2
v4 = v1+ v2 + v3
print(v4)'''
'''Create a small program where invalid user input raises a custom exception,
logs the error, and continues execution instead of crashin'''
class Invaliduserinput(Exception):
    def __init__(self,message="user input provided is invalid please provide a valid input"):
        self.message = message
        super().__init__(message)

try:
    string = input("enter a string")
    if not string.isdigit():
        raise Invaliduserinput()

except Invaliduserinput as e:
    print("logged error", e)

print("the program continues...")
