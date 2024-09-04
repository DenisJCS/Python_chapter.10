#this is exception block that allow run program even if Python thinks it as error
try:
    print(5/0)
except: ZeroDivisionError
print("You can't divide by zero")

#Calculator does only division

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    
#Here new version of program that take exception block
try:
    print(5/0)
except: ZeroDivisionError
print("You can't divide by zero")

#Calculator does only division

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide bu 0!")
    else:
        print(answer)
        
# From terminal 
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 7

Second number: 2
3.5

First number: 13

Second number: 3
4.333333333333333

First number: 5

Second number: 0
You can't divide bu 0!


