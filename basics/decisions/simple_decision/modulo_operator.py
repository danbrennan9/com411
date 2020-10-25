def run():
  print("Please enter a whole number.") #inout from user
  number = int(input())

  if (number % 2 == 0):
    print("The number {} is even!".format(number)) #first check, if false, moves to elif

  elif (number % 2 == 1):
    print("The number {} is odd!".format(number)) #second check, if false moves to else

  else: # to account for human error
    print("I'm not sure what you mean.")