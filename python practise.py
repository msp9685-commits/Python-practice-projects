"""Write a program that asks the user for a number and prints whether it is
positive, negative, or zero"""
'''num = int(input("Enter a number"))
if(num > 0):
    print(f"entered number {num} is poistive")
elif(num<0):
    print(f"entered number {num} is negative")
else :
    print(f"entered number {num} is zero")'''
"""Create a program that checks if a person is eligible to vote (age >= 18).
"""
'''age = int(input("Enter your current age"))
if(age >= 18):
    print("you are eligible for voting")
elif(age < 0):
    print("please enter a valid age")
else :
    print("sorry you are not eligible for voting")'''
'''Ask the user to enter a day number (1–7) and print the corresponding day of
the week using match case .'''
'''day = int(input("please enter day number"))
match day :
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Sunday")
    case _:
        print("invalid")
    '''
'''Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case .'''
'''a = int(input("please enter a number"))
b = int(input("please enter another number"))
oper = input("enter a operator +/-/*/(/)")
match oper:
    case "+":
        print(f"sum of {a} and {b} is = {a+b}")
    case "-":
        print(f"{a} - {b} is = {a-b}")
    case "*":
        print(f"{a} * {b} is =  {a*b}")
    case "/":
        print(f"{a} / {b} is = {a/b}")
    case _:
        print("invalid operator")'''
'''Print numbers from 1 to 10 using a for loop'''
'''Print the multiplication table of a number (entered by user)'''
'''a = int(input("enter a number"))
for i in range(1, 11):
    print(a*i)'''
'''Calculate the sum of all numbers from 1 to 100 using a for loop
sum = 0
for i in range(1,101):
    sum += i
print(sum)'''
'''
Print the following pattern using a for loop
*
**
***
****
for a in range(1, 5):
    print("*" * a)'''
'''Print numbers from 1 to 10 using a while loop'''
'''Write a program that keeps asking the user to enter a password until they
enter the correct one
password = input("enter  your password\n")
while password != "password":
    password = input("enter  your password\n")
'''
'''Use a while loop to reverse a given number (e.g., 123 → 321'''
'''Use a for loop to print numbers from 1 to 10, but stop the loop if the
number is 7 (use break ).
for a in range(1,11):
    print(a)
    if a == 7:
        break'''
'''Print numbers from 1 to 10, skipping the number 5 (use continue '''
'''for a in range(1,11):
    if a == 5:
        continue
    print(a)'''
'''a =1
while(a<11):
    if a ==5:
        a += 1
        continue
    print(a)
    a+=1'''
'''Write a loop that goes through numbers 1 to 5, but does nothing for number
3
i = 2
for a in range(1,11):
    if a == 3:
        pass
    else:
        print(a)'''

'''num = input("enter a number")
num1 = num[::-1]

print(int(num1))'''
'''Create a string variable name with your full name. Print:
The first character
The last character
The length of the string'''
'''name = "Ayush Singh"
print(name[0])
print(name[-1])
print(len(name))'''
'''Concatenate two strings: "Hello" and "World" with a space in between'''
'''print("hello" + " " + "world")
a = "hello"
b = "world"
print(f"{a} {b}")'''
'''text = ("hello","world")
new = " ".join(text)
print(new)'''
'''Given text = "Python Programming" , do the following:
Print the first 6 characters
Print the last 6 characters
Print every second character from the string

text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[::2])
print(text[::-1])'''
'''Take the string " i love python programming " and:
Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
string = " i love python programming "
new = string.strip()
print(new)
print(new.title())
print(new.lower().count("o"))'''
'''Check if the string "123abc" is alphanumeric.
string = "\t\n"
print(string.isalnum())
print(string.isalpha())
print(string.isdigit())
print(string.isspace())'''
'''Using format() , create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.
print("My name is {} and I am {} years old".format("John", 25))'''
'''Given sentence = "Coding in Python is fun" , replace "fun" with
"awesome" and print it
Find the index of the word "Python" in sentence .
Convert the entire sentence to uppercase and print it 
sentence = "Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.find("Python"))
print(sentence.upper())'''
'''Write a program that counts how many vowels are in a given string
string = "My name is John and I am 25 years old."
count = 0
count += string.count("a") + string.count("e") + string.count("o") + string.count("u") + string.count("i")
print(count)'''
'''Take a user input string and check if it is a palindrome (same forwards and
backwards
str = input("enter a string ")
str_rev = str[::-1]
if str == str_rev:
    print("palindrome")
else:
    print("not a palindrome")'''
'''Write a function greet() that prints "Hello, Python Learner!" when
called
def greet():
    print("Hello, Python Learner!")

greet()'''
'''Write a function square(num) that returns the square of a given number. Test
it with different numbers.
def square(num):
    return num * num
print(square(33))'''
'''Write a function full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format "First Last"
def full_name(first, last):
    str = (first,last)
    conc_str = " ".join(str)
    return conc_str
print(full_name("Ayush", "Singh"))'''
'''Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)
def calculate_area(length, width=10):
    return length * width
print(calculate_area(5,45))'''
'''Write a lambda function that adds two numbers and test i
sum = lambda x, y : x + y
print(sum(4,5))'''
'''Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their square'''
'''Write a recursive function factorial(n) that returns the factorial of a
number.
def rec(n):
    if n==1:
        return 1
    else:
        return n * rec(n-1)
    
print(rec(3))'''
'''Write a recursive function sum_of_digits(n) that returns the sum of all digits
of a given number.'''
def sum_of_digits(n):
    pass
'''Import the math module and use it to:
Find the square root of 144
Calculate sin(90°) (hint: use math.radians() )
import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))'''
'''Install and import the requests module (if available) and use it to fetch data
from "https://api.github.com"
import requests
response = requests.get("https://api.github.com")
print(response)
print(response.status_code)
data = response.json()
print(data["current_user_url"])
print(data["repository_url"])'''
'''print(data["repository_url"])'''
'''Write a recursive function fibonacci(n) that prints the first n Fibonacci
numbers'''
def fib(n):
    sum = 0
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        sum += fib(n-1) + fib(n-2)
        return sum
    
n = int(input("Enter n: "))
for i in range(n):
    print(fib(i))
