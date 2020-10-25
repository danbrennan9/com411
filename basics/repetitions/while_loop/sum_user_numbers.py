def run():
  print("How many numbers should I sum up?")
  numbers_to_sum = int(input()) #getting sum of variable through user input

  summed = 0 #used to repeat while loop

  total = 0

  while (summed <= numbers_to_sum):
    print("Please enter a number from", summed, "of", numbers_to_sum) #loops to gain user input of what numbers they'd wish to add
    number = int(input()) #the variable used to control each number the user inputs
    total = total + number #total of all the numbers added together
    summed = summed + 1 #the loop 

  print("The answer is {}".format(total)) #shows answer
