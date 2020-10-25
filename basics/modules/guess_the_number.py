import random as rnd

print("Please enter the minimum value.")
min_value = int(input())

print("Please enter the maximum value.")
max_value = int(input())

correct_guess = rnd.randrange(min_value, max_value, 1)

print("I am thinking of a number between {} and {}. Can you guess what it is?".format(min_value, max_value))

guess = 0

while(guess != correct_guess):
  print("Please enter a number:")
  guess = int(input())

  if (guess == correct_guess):
    print("Congratulations!")
    break
  
  elif (guess < correct_guess):
    print("Guess higher!")

  else:
    print("Guess lower!")

print("Game over!")