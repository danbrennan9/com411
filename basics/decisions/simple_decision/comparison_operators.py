print("Please enter the first number.") #input of first number
first_number = int(input())

print("Please enter the second number.") #input of second number
second_number = int(input())

if (first_number < second_number): #checks to see if first number is smaller than second number, if true ends program, if false moves to next elif statement
  print("The first number is the smallest!")

elif (first_number > second_number): #checks to see if first number is bigger than second number, if true ends program if false moves to else statementw
  print("The second number is the smallest!")

else: #if both if and elif statement are false, the else statement must be true
  print("Both are equal!")