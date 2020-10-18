print("Please enter a whole number.")
number = int(input())

if (number % 2 == 0):
  print("The number {} is even!".format(number))

elif (number % 2 == 1):
  print("The number {} is odd!".format(number))

else:
  print("I'm not sure what you mean.")