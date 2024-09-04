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
    
denis_jcs@Deniss-MacBook-Air chapter_10 % python3 division_calculate.py
You can't divide by zero
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 250

Second number: 15
16.666666666666668

First number: 9999

Second number: 1717
5.823529411764706

First number: q
denis_jcs@Deniss-MacBook-Air chapter_10 % 

#But this program does nothing to handle errors so asking it to divide by zero
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 10

Second number: 50
0.2

First number: 100

Second number: 0
Traceback (most recent call last):
  File "/Users/denis_jcs/Desktop/chapter_10/division_calculate.py", line 18, in <module>
    answer = int(first_number) / int(second_number)
             ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
