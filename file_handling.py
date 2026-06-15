'''Create a text file notes.txt using Python and write "Learning Python is
fun!" into it.

file = open("notes.txt", "w")
file.write("Learning Python is fun!")
file.close()
Open notes.txt , read its content, and print it to the console
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()'''
'''write a program that writes three lines of text to a file tasks.txt .
Open tasks.txt in append mode and add a new line "Task Completed!" .
Read the file and print all lines as a list using readlines()
with open("tasks.txt", "w") as file:
    file.write("hey this is python code\n" "the code contains three lines \n" "this is third line\n")

with open("tasks.txt", "a") as file:
    file.write("Task Completed!")

with open("tasks.txt", "r") as file:
    content = file.readlines()
    content = [line.strip() for line in content]
    for line in content:
        print(line)
'''
'''Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder
import os
print(os.getcwd())
print(os.listdir())
os.mkdir("my_folder")'''
'''Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!
import shutil
import os
shutil.copy("tasks.txt", "my_tasks.txt")

os.remove("my_task.txt")'''
'''Write a small script count_lines.py that takes a filename as input and prints
how many lines are in the file'''
