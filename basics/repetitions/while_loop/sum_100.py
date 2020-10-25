def run():
  print("Calculating the sum of the first 100 numbers...")

  numbers = 1 #counting variable used for loop

  total = 0 #total variable

  while (numbers <= 100): #while number is less than 100, loop continues
    total = total + numbers #sums the total, so in the first case numbers has 1, plus total (0) = 1
    numbers = numbers + 1 #adds one to numbers, to continue loop

  print("Done! The answer is {}".format(total)) #presents total